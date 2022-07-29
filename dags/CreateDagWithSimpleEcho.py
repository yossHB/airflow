from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator



default_args = {
    'owner' : 'yosr',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)
}

with DAG(
    dag_id = 'Second_one__',
    default_args=default_args,
    description='This is my second airflow project',
    start_date=datetime(2021,7,29,2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, I'm the first task",
    ) 

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hello world, i'm the second task and i'm going to run after the first task",
    ) 
    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo hello world, i'm the third task and i'm going to run after the first task",
    ) 
    task4 = BashOperator(
        task_id='foor_task',
        bash_command="echo hello world, i'm nmbr 4 task and i'm going to run after the second task",
    ) 
    task1.set_downstream(task2)
    task1.set_downstream(task3)
    # task2.set_downstream(task4)
    task2 >> task4
