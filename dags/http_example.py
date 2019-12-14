
import airflow
from airflow.models import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.operators.python_operator import PythonOperator


import requests
import json
from datetime import datetime

args = {
    'owner': 'Bruno Andrade',
    'start_date': datetime(2019, 12, 10),
    'depends_on_past': False
}

dag = DAG(
    dag_id='http_example_aifest',
    default_args=args,
    schedule_interval='0 12 * * *'
)


def save_response(ti, ds, **kwargs):
    response = ti.xcom_pull(task_ids='get_joke')
    open(f'joke_{ds}_http.json', 'w').write(response)

    return "OK!"

run_this = SimpleHttpOperator(
    task_id='get_joke',
    method='GET',
    xcom_push=True,
    dag=dag,
    endpoint='jokes/random',
    log_response=True
)

run_that = PythonOperator(
    task_id='save_joke',
    python_callable=save_response,
    provide_context=True,
    dag=dag
)

run_this >> run_that