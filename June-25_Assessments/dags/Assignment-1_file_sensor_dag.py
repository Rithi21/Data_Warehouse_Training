from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import shutil
import pandas as pd

# Define paths
INCOMING_FILE = '/opt/airflow/data/incoming/report.csv'
ARCHIVE_FOLDER = '/opt/airflow/archive/'

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

def process_file():
    # Read and print content of the CSV file
    df = pd.read_csv(INCOMING_FILE)
    print("File contents:")
    print(df.head()) 

def move_to_archive():
    if not os.path.exists(INCOMING_FILE):
        raise FileNotFoundError(f"{INCOMING_FILE} does not exist.")
    if not os.path.exists(ARCHIVE_FOLDER):
        os.makedirs(ARCHIVE_FOLDER)
    shutil.move(INCOMING_FILE, os.path.join(ARCHIVE_FOLDER, 'report.csv'))
    print("File moved to archive.")

with DAG(
    dag_id='file_sensor_pipeline',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None, 
    catchup=False
) as dag:

    wait_for_file = FileSensor(
        task_id='wait_for_report_file',
        filepath='data/incoming/report.csv',
        fs_conn_id='fs_default',  
        poke_interval=30,  # check every 30 seconds
        timeout=600,  # 10 minutes
        mode='poke',
        soft_fail=True  
    )

    process = PythonOperator(
        task_id='process_file',
        python_callable=process_file
    )

    archive = PythonOperator(
        task_id='move_to_archive',
        python_callable=move_to_archive
    )

    wait_for_file >> process >> archive
