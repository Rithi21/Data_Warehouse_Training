from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

def parent_task():
    print("Parent DAG task executed.")

with DAG(
    dag_id='parent_dag',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='do_parent_task',
        python_callable=parent_task
    )

    trigger_child = TriggerDagRunOperator(
        task_id='trigger_child_dag',
        trigger_dag_id='child_dag',
        conf={"triggered_date": "{{ ds }}"},  # Pass execution date
        wait_for_completion=False
    )

    task1 >> trigger_child
