HttpSensor and Notes about Connections

# HttpSensor and Notes about Connections
+ All tasks have a `task_id`
+ **`http_conn_id` is a connection that is defined in the Airflow Web UI**
+ `response_check` is a function that defines the success of the Sensor
+ `poke_interval` and `timeout` are used for Sensor tasks