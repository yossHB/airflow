mimo@ubuntu:~/airflow$ sudo su - postgres
postgres@ubuntu:~$ psql



to open the back using the docker command:
     docker exec -it 720e07b2f07f bash
to backfill the gag run:
     airflow dags backfill -s 2022-01-01 -e 2022-02-01 dag_with_catchup_backfill

