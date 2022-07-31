# connect to external servers

from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    'owner': 'yosr',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_postgres_operator',
    default_args=default_args,
    start_date=datetime(2022, 1, 1),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id='postgres_localhost',
        sql="/data/postgres/pet_schema.sql",
    )

    task2 = PostgresOperator(
        task_id='insert_into_table', 
        postgres_conn_id='postgres_localhost',
        sql="""
            insert into dag_runs (dt, dag_id) values ('{{ ds }}', '{{ dag.dag_id }}')
        """
    )

    task3 = PostgresOperator(
        task_id='delete_data_from_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            delete from dag_runs where dt = '{{ ds }}' and dag_id = '{{ dag.dag_id }}';
        """
    )
    task1 >> task3 >> task2



# docker network create app-net
# docker run -d --net app-net --name host.docker.local -p 5432:5432 postgres
# 

