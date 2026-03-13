from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def ingest():
    print("Fetch OpenSky data")

def train():
    print("Train transformer model")

dag = DAG(
    "aviation_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily"
)

task1 = PythonOperator(
    task_id="data_ingestion",
    python_callable=ingest,
    dag=dag
)

task2 = PythonOperator(
    task_id="model_training",
    python_callable=train,
    dag=dag
)

task1 >> task2