docker-compose up 



# airflow


### resource
- postgres setup
    - https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart


- connect to postgresql data in bdeaver
    - 


### solution
- FATAL: password authentication failed for user "airflow" FATAL: password authentication failed for user "airflow"
    - alter user airflow with password 'airflow';

### schema
|-- airflow
   |-- dags
   |-- logs
   |-- plugins
   |-- data
      |-- airflow
         -- check_init.sql
         -- set_init.sql
         -- init.sh
      |-- postgres
         -- 00_init.sql
    -- Dockerfile
    -- docker-compose.yml
    -- airflow.env
    -- airflow_db.env
    -- postgres.env

### ways to install python dependencies to your airflow docker container
    - image extending
    - image customising

