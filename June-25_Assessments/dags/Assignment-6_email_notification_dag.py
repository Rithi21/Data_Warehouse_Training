from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta
from airflow.models import Variable
import logging

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'email_on_failure': True,
    'email': [Variable.get("email_recipients", default_var="fallback@example.com")]
}

def task_1():
    logging.info("Task 1 is running.")

def task_2():
    logging.info("Task 2 is running.")
    # Uncomment to test failure alert
    # raise Exception("Simulated failure!")

with DAG(
    dag_id='email_notification_workflow',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id='task_1',
        python_callable=task_1
    )

    t2 = PythonOperator(
        task_id='task_2',
        python_callable=task_2
    )

    send_success_email = EmailOperator(
        task_id='send_success_email',
        to=Variable.get("email_recipients", default_var="fallback@example.com"),
        subject='DAG Success: email_notification_workflow',
        html_content="""<h3>All tasks completed successfully</h3>""",
        trigger_rule='all_success' 
    )

    [t1, t2] >> send_success_email
