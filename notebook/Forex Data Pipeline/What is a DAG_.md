What is a DAG?

# What is a DAG?
+ Collection of tasks with schedule and dependencies between them
+ __Node = Task__
+ __Edge = Dependency__

# Important Properties of DAG
+ `dag_id` unique id of DAG
+ `description`
+ `start_date` indicates from which date your DAG should start
+ `schedule_interval` defines how often DAG runs from the start_date
+ `default_args` dictionary containing parameters that will be applied to all operators and so to your tasks
+ `catchup` to perform scheduler catchup

# Steps for Minimal DAG
+ Instantiate a DAG object
+ Implement tasks with operators
+ Add dependencies between tasks

# Minimum Parameters that you should always provide
+ `default_args` - is a dict
	+ `owner` (should have an airflow unix user)
	+ `start_date`
	+ `depends_on_past` - tells the task to run even if the last run of the task has failed
	+ `email_on_failure`
	+ `email_on_retry`
	+ `email` - need this just in case, can be set to the wrong email
	+ `retries` - how many times to try to retry
	+ `retry_delay`
+ `dag_id`
+ `schedule_interval`
+ `catchup`

__Use a context manager for DAG__
`with DAG(...) as dag:`