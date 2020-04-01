Installation Notes

## Installation Notes
+ `export AIRFLOW_HOME=...` tells Airflow where the configuration files are stored as well as the DAGs
+ Install the dependencies used for Airflow
+ if not using Docker, make a user for Airflow
+ can use square brackets with `pip install apache-airflow` to install subpackages with it
	+ for this course: `[crypto,celery,postgres,hive,mysql,ssh,docker,hdfs,kubernetes,redis,rabbitmq,slack]`

### Initialize Airflow and start everything that we need:
_Run the scheduler on one, and the webserver on another docker container in production, but within the same machine_
+ `airflow initdb`
+ `airflow scheduler` (can also run in background which makes the most sense for this use case `airflow scheduler &> /dev/null &` or even use screen if you want to be able to see the outputs! I like that better for debugging purposes)
+ `airflow webserver` (we run this in the foreground for the docker logs)

## see airflow-materials/airflow-basic for the super basic Docker install of Airflow

## IN PRACTICE:
+ Webserver on one container
+ Scheduler on another container (on the same machine is OK)
+ MetadataDB on a different container on a SEPARATE MACHINE to make sure that everything is safe if one machine fails