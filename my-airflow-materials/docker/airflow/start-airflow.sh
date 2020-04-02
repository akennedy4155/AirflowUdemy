#!/usr/bin/env bash

# Create the user airflow in the HDFS
# hdfs dfs -mkdir -p    /user/airflow/
# hdfs dfs -chmod g+w   /user/airflow

# Move to the AIRFLOW HOME directory
cd $AIRFLOW_HOME

# Install the custom module
pip install -e /usr/local/python/forex

# Initiliase the metadatabase
airflow initdb

# Make the Forex connection
airflow connections -a --conn_id "forex_api" --conn_host "api.exchangeratesapi.io" --conn_type "http"

# Run the scheduler in background
airflow scheduler &> /dev/null &

# Run the web sever in foreground (for docker logs)
exec airflow webserver