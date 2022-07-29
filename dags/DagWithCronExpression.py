# https://crontab.guru/   gives a visual way to generate and verify the cron expression
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'yosr',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id="dag_with_cron_expression",
    start_date=datetime(2022, 1, 1),
    schedule_interval='0 3 * * Tue-Fri'   # “At 03:00 on every day-of-week from Tuesday through Friday.”
    #schedule_interval='0 3 * * Tue,Fri'   # “At 03:00 on Tuesday and Friday.”
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression!"
    )
    task1