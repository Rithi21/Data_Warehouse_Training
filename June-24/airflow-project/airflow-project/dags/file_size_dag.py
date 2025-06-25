from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime
import os

FILE_PATH = '/opt/airflow/data/inventory.csv'
SIZE_THRESHOLD_KB = 500  # 500KB

def check_file_size():
    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f"{FILE_PATH} not found.")
    file_size_kb = os.path.getsize(FILE_PATH) / 1024
    print(f"File size: {file_size_kb:.2f} KB")
    return 'light_summary' if file_size_kb < SIZE_THRESHOLD_KB else 'detailed_processing'

def light_summary():
    print("Performing light summary on small file.")

def detailed_processing():
    print(" Running detailed processing on large file.")

def cleanup():
    print("Cleaning up after processing.")

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False
}

with DAG(
    dag_id='branching_file_size_dag',
    default_args=default_args,
    schedule_interval=None,
    description="Branching DAG based on inventory file size",
    tags=['branching', 'filesize']
) as dag:

    start = BranchPythonOperator(
        task_id='check_file_size',
        python_callable=check_file_size
    )

    light = PythonOperator(
        task_id='light_summary',
        python_callable=light_summary
    )

    heavy = PythonOperator(
        task_id='detailed_processing',
        python_callable=detailed_processing
    )

    cleanup_task = PythonOperator(
        task_id='cleanup',
        python_callable=cleanup,
        trigger_rule='none_failed_or_skipped'  
    )

    end = EmptyOperator(task_id='end')

    start >> [light, heavy]
    light >> cleanup_task
    heavy >> cleanup_task
    cleanup_task >> end
