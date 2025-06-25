from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import os

ORDERS_PATH = '/opt/airflow/data/orders.csv'
REQUIRED_COLUMNS = ['order_id', 'customer_id', 'order_date', 'amount']
MANDATORY_FIELDS = ['order_id', 'customer_id', 'order_date']

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

def validate_data():
    if not os.path.exists(ORDERS_PATH):
        raise FileNotFoundError(f"{ORDERS_PATH} not found")

    df = pd.read_csv(ORDERS_PATH)

    # Step 2: Validate columns
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")

    # Step 3: Check for nulls in mandatory fields
    for col in MANDATORY_FIELDS:
        if df[col].isnull().any():
            raise ValueError(f"Null values found in mandatory field: {col}")

    print("Data validation passed.")

def summarize_orders():
    df = pd.read_csv(ORDERS_PATH)
    summary = df.groupby('customer_id')['amount'].sum().reset_index()
    print("Order summary:")
    print(summary)

with DAG(
    dag_id='data_quality_validation',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    validate = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data
    )

    summarize = PythonOperator(
        task_id='summarize_orders',
        python_callable=summarize_orders
    )

    validate >> summarize
