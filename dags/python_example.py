import airflow
from airflow.models import DAG
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
    dag_id='python_example_aifest',
    default_args=args,
    schedule_interval='0 12 * * *'
)


def get_chuck_norris_joke(ds, **kwargs):
    response = requests.get('https://api.icndb.com/jokes/random')
    open(f'joke_{ds}_python.json', 'w').write(json.dumps(response.json()))

    return 'OK!'


run_this = PythonOperator(
    task_id='get_joke',
    provide_context=True,
    python_callable=get_chuck_norris_joke,
    dag=dag
)
