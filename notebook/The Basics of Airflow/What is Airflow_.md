What is Airflow?

# What is Airflow?
+ Author, schedule, monitor data pipelines
+ Defined as code and tasks are instantiated dynamically


## CORE COMPONENTS

### Web Server 
+ Flask server runs with Gnuicorn and serves the UI dashboard

### Scheduler
+ Daemon responsible with scheduling jobs

### Metadata Database 
+ all metadata related to the admin and jobs are stored and must be supported by SQLAlchemy library

### Executor 
+ Defines how tasks are executed

### Worker
+ Process executing the tasks, determined by the executor


## KEY CONCEPTS

### DAG 
+ a graph object representing the data pipeline

### Operator 
+ single task in the data pipeline

### Task 
+ instance of operator

### Task Instance 
+ specific run of a task = DAG + TASK + POINT IN TIME

### Workflow 
+ combination of everything above


## What Airflow brings me?

+ Dynamic pipelines configured with Python

+ Graphical representation of DAGs and metrics

+ Scalable with the right configuration (we will see later) run in parallel distributed

+ Backfill - ability to run DAG form the past to "backfill" until a point in time

+ Airflow is extensible.  New operators bring new functionalities (modular)


## What Airflow IS NOT:

+ Not a data streaming solution (not like spark or storm)
+ Built to perform scheduled batch jobs