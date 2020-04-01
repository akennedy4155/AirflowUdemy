Airflow CLI

# Airflow CLI

## Some cool common ones
+ `airflow initdb`
	+ sets up the different tables that power Airflow
+ `airflow resetdb`
	+ rebuild the metadata DB
	+ _BE CAREFUL_ like a fresh install... gets rid of everything
+ `airflow upgradedb`
	+ upgrade the metastore DB
	+ used for updating the version of Airflow
	+ changing executor, etc.
+ `airflow webserver`
	+ `-p` specify the port
	+ `-w` specify the number of gnuicorn workers that we want
	+ `-d` debug mode
+ `airflow scheduler`
	+ `-d` debug mode
	+ `-sd` where to look for DAGs
+ `airflow worker`
	+ where tasks are executed (for using Celery executor)

	
## More advanced CLI
+ `airflow list_dags`
	+ list of all the DAGs that airflow is aware of
+ `airflow trigger_dag <some_dag>`
	+ `-e` specify a date in the past
		+ leads to the DAG executing as many times as it needs to from the date specified to catch up to the current schedule interval
		+ called __catch-up__ and __backfilling__
+ `airflow list_dag_runs <dag>`
+ `airflow list_tasks <dag>`
+ `airflow test <dag> <task> <execution date in the past>`
	+ test a task instance without checking for dependencies and without storing anything in the metadata DB
	+ get the output produced by the output of that task as if it were run with the scheduler
	+ useful for CI/CD for testing before merging to the master/feature branch