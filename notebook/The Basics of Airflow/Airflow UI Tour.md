Airflow UI Tour

# Airflow UI Tour
`airflow.cfg` has configuration for all sorts of things relating to the Docker webserver, ports etc.

## Main Page
+ overview of tasks
	+ schedule
	+ success, failure, resume etc.

## Cool tips
+ If the job is switched off, you won't even be able to trigger it manually
+ `Clear` button in the task details from the graph view is the recommended way to re-run a task
	+ Deletes the previous state of the task instance allowing it to get re-triggered by the scheduler or a backfill command
+ `Delete` button gets rid of all of the metadata associated with this DAG without actually getting rid of the DAG itself.  __CAUTION__
+ `Refresh` gets the latest version of the DAG
+ `Details` View for dag shows the file path of the DAG on the machine
+ Clear DAG Runs by going to `Browse->Task Instances` and clearing all the selected for the DAG that you want to clear.  Then, go to the `DagRuns` GUI and delete the DAGs for this task.