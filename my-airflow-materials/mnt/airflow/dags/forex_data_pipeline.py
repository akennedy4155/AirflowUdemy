from os import path
from datetime import datetime, timedelta

from airflow import DAG
from airflow.sensors.http_sensor import HttpSensor
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.python_operator import PythonOperator

from api_download.APIToJSON import APIToJSON

# define the default arguments that are used in all tasks of the DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime.now() - timedelta(1),
    # tells the task to run even if the last run of the task has failed
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    # need this just in case we do want to send emails even if the previous is set to false
    "email": "youremail@host.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

# instantiate the DAG object
with DAG(
    dag_id="forex_data_pipeline",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False
) as dag:
    # None because we haven't defined any tasks yet
    forex_rates_available = HttpSensor(
        task_id='forex_rates_available',
        method='GET',
        http_conn_id='forex_api',
        endpoint='latest',
        response_check=lambda response: "rates" in response.text,
        poke_interval=5,
        timeout=20,
    )
    forex_file_dropped = FileSensor(
        task_id="forex_file_dropped",
        filepath="forex_currencies.csv",
        fs_conn_id="forex_path",
        poke_interval=5,
        timeout=20
    )
    fp = path.join('/', 'usr', 'local', 'airflow', 'dags', 'files')
    forex_api_download = PythonOperator(
        task_id='forex_api_download',
        python_callable=APIToJSON(
            config_path=path.join(fp, 'forex_currencies.csv'),
            conn_id="forex_api",
        ).dl_and_write,
        provide_context=True,
        op_kwargs={'output_path': path.join(fp, 'forex_rates.json')}
    )
