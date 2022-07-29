from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

with DAG(
    'first_pipeline',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    t1 = BashOperator(
        task_id='Begin_execution',
        bash_command='date',
    )
    t2 = BashOperator(
        task_id='Stage_events',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )
    t1.doc_md = dedent(
        """\
    #### Task Documentation
    You can document your task using the attributes `doc_md` (markdown),
    `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    rendered in the UI's Task Instance Details page.
    ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)

    """
    )

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG
    dag.doc_md = """
    This is a documentation placed anywhere
    """  
    # otherwise, type it like this
    templated_command = dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
    {% endfor %}
    """
    )

    t3 = BashOperator(
        task_id='Stage_songs',
        depends_on_past=False,
        bash_command=templated_command,
    )
    
    t4 = BashOperator(
        task_id='Laad_songplays_fact_table',
        depends_on_past=False,
        bash_command='sleep 8',
    )
    
    t5 = BashOperator(
        task_id='Load_artist_dim_table',
        depends_on_past=False,
        bash_command='templated_command',
    )
    
    t6 = BashOperator(
        task_id='Load_time_dim_table',
        depends_on_past=False,
        bash_command='sleep 16',
    )

    t7 = BashOperator(
        task_id='Load_song_dim_table',
        depends_on_past=False,
        bash_command='sleep 16',
    )
    
    t8 = BashOperator(
        task_id='Run_data_quality_checks',
        depends_on_past=False,
        bash_command='sleep 16',
    )

    t9 = BashOperator(
        task_id='Stop_execution',
        depends_on_past=False,
        bash_command='sleep 16',
    )

    t1 >> [t2, t3]
    t2 >> t4
    t3 >> t4
    t4 >> [t5, t6,t7]
    t5 >> t8
    t6 >> t8
    t7 >> t8
    t8 >> t9
