from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.sensors.http_sensor import HttpSensor
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import json
import logging
import os

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(seconds=15)
}

def parse_and_save_data(response_text, **kwargs):
    try:
        data = json.loads(response_text)
        price = data['bpi']['USD']['rate']
        time = data['time']['updated']
        output = f"{time} - Bitcoin Price (USD): ${price}"
        logging.info(output)

        os.makedirs("/opt/airflow/data", exist_ok=True)
        with open("/opt/airflow/data/btc_price.txt", "w") as f:
            f.write(output)

    except Exception as e:
        raise ValueError(f"Failed to parse or write data: {str(e)}")

with DAG(
    dag_id='external_api_interaction',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@hourly',
    catchup=False
) as dag:

    check_api = HttpSensor(
        task_id='check_api',
        http_conn_id='coindesk_api',
        endpoint='v1/bpi/currentprice.json',
        response_check=lambda r: r.status_code == 200,
        poke_interval=10,
        timeout=60
    )

    get_price = SimpleHttpOperator(
        task_id='get_bitcoin_price',
        http_conn_id='coindesk_api',
        endpoint='v1/bpi/currentprice.json',
        method='GET',
        response_filter=lambda response: response.text,
        log_response=True
    )

    parse_and_log = PythonOperator(
        task_id='parse_and_save',
        python_callable=parse_and_save_data,
        op_args=['{{ ti.xcom_pull(task_ids="get_bitcoin_price") }}'],
        provide_context=True
    )

    check_api >> get_price >> parse_and_log
