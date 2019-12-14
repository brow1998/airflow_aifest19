import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

args = {
    'owner': 'Bruno Andrade',
    'start_date': datetime(2019, 12, 10),
    'depends_on_past': False
}

dag = DAG(
    dag_id='bash_example_aifest',
    default_args=args,
    schedule_interval='0 12 * * *'
)

run_this = BashOperator(
    task_id='get_joke',
    bash_command='wget https://api.icndb.com/jokes/random -O /tmp/joke_{{ds}}_bash.json',
    dag=dag
)
