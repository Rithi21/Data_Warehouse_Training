from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time
import logging
import random

default_args = {
    'owner': 'airflow',
    'retries': 3,                            
    'retry_delay': timedelta(seconds=10),      
    'retry_exponential_backoff': True,       
    'max_retry_delay': timedelta(minutes=5),  
}

def long_running_task():
    sleep_time = random.randint(15, 45) 
    logging.info(f"Task sleeping for {sleep_time} seconds...")

    time.sleep(sleep_time)
    
    if sleep_time > 30:
        logging.error("Simulated failure due to timeout risk.")
        raise Exception("Task took too long and failed intentionally.")

    logging.info("Task completed successfully.")

with DAG(
    dag_id='retry_and_timeout_handling',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    task_with_timeout = PythonOperator(
        task_id='simulate_long_running_task',
        python_callable=long_running_task,
        execution_timeout=timedelta(seconds=30),  
    )
