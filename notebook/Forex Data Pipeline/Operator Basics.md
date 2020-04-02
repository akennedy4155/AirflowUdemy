Operator Basics

# What is an Operator
+ Describes what actually gets done in a task
	+ Defines a _single task_
+ Describes a single task in a data pipeline
+ __Atomic__ - doesn't need to share resources with any other operators
+ Run independently
	+ Could run on different machines for scalability
+ __Idempotent__
	+ Same result regardless of how many times it is run
+ Retry automatically if needed and specified
+ __Task is created by instantiating an Operator class__
+ When instantiated, the task becomes a node in the DAG

## All Tasks must have a task_id (doesn't need to be the same as the variable name in Python)

# Airflow Provides Many Operators
+ BashOperator
+ PythonOperator
+ Email Operator
+ MySQL, PostgresOperator...
	+ many different db connections can be made

	
# Types of Operators
+ All classes inherit from `BaseOperator`
+ Types of operators
	+ Action Operators
		+ perform some action
	+ Transfer Operator
		+ moving data from one system to another
		+ __Important Note about Transfer Operators!__
			+ move data by pulling from source, stage on machine where the executor is running, and then transferred to the target system
			+ Don't use these operators if you're dealing with a large amount of data!
	+ Sensor Operator
		+ waiting for something to happen
		+ long running task
		+ example: waiting for a file to arrive
		+ BaseSensorOperator
		+ __has a 'poke' method__