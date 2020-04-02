import pytest
from os import path

from airflow.models import Connection
from airflow.hooks.base_hook import BaseHook
from airflow.hooks.http_hook import HttpHook

from api_download.APIToJSON import APIToJSON

test_dir = path.join('/', 'home', 'alex', 'Documents', 'AirflowUdemy', 'my-airflow-materials', 'docker', 'airflow',
                  'forex', 'api_download', 'tests')


@pytest.fixture()
def atj(mocker):
    mocker.patch.object(
        BaseHook,
        "get_connection",
        return_value=Connection(schema="https", host="api.exchangeratesapi.io")
    )
    return APIToJSON(
        path.join(test_dir, 'files', 'cfg.csv'),
        '2020-03-31',
        "forex_api"
    )


def test__parse_cfg(atj):
    assert atj.cfg == {
        "EUR": ['USD', 'NZD', 'JPY', 'GBP', 'CAD']
    }


def test__download_api(atj):
    assert atj.rate_json[0] == {
        "rates": {
            "NZD": 1.8417,
            "CAD": 1.5617,
            "JPY": 118.9,
            "USD": 1.0956,
            "GBP": 0.88643},
        "base": "EUR",
        "date": "2020-03-31"
    }


def test_write_json(atj):
    json_fp = path.join(test_dir, 'files', 'test_json.json')
    atj.write_json(json_fp)
    assert path.exists(json_fp)
