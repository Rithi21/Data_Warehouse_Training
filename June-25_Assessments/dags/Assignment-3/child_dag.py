from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

def child_task(**kwargs):
    conf = kwargs.get('dag_run').conf
    triggered_date = conf.get('triggered_date', 'Not provided')
    print(f"Child DAG triggered with date: {triggered_date}")

with DAG(
    dag_id='child_dag',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='do_child_task',
        python_callable=child_task,
        provide_context=True  
    )
