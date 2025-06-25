from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta
import logging

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

def check_time_and_branch(**kwargs):
    now = datetime.now()
    day_of_week = now.weekday()  # Monday = 0, Sunday = 6

    if day_of_week >= 5:  # Saturday or Sunday
        logging.info("It's the weekend. Skipping DAG.")
        return 'skip_dag'

    current_hour = now.hour
    logging.info(f"Current hour: {current_hour}")

    if current_hour < 12:
        return 'morning_task'
    else:
        return 'afternoon_task'

def morning_task():
    logging.info("Running morning task (Task A)")

def afternoon_task():
    logging.info("Running afternoon task (Task B)")

def final_cleanup():
    logging.info("Performing final cleanup")

with DAG(
    dag_id='time_based_conditional_tasks',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@hourly',  # or use cron like '0 * * * *'
    catchup=False
) as dag:

    start = BranchPythonOperator(
        task_id='check_time_and_branch',
        python_callable=check_time_and_branch,
        provide_context=True
    )

    skip = EmptyOperator(
        task_id='skip_dag'
    )

    morning = PythonOperator(
        task_id='morning_task',
        python_callable=morning_task
    )

    afternoon = PythonOperator(
        task_id='afternoon_task',
        python_callable=afternoon_task
    )

    cleanup = PythonOperator(
        task_id='final_cleanup',
        python_callable=final_cleanup,
        trigger_rule='none_failed_min_one_success'  # ensures cleanup runs regardless of branch
    )

    start >> [skip, morning, afternoon]
    morning >> cleanup
    afternoon >> cleanup
    skip >> cleanup
