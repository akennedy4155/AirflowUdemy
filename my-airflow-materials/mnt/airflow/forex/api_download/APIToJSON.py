import csv
import logging
import json
from urllib.parse import urlencode

from airflow.hooks.http_hook import HttpHook


class APIToJSON:
    def __init__(self, config_path, conn_id):
        self.config_path = config_path
        self.endpoint = None
        self.conn_id = conn_id

        self.cfg = self._parse_cfg()

    def _parse_cfg(self):
        logging.info('Parsing config file.')
        cfg = {}
        # parse currency config to dict
        with open(self.config_path) as f:
            csv_reader = csv.reader(f, delimiter=';')
            next(csv_reader, None)  # skip the header
            for row in csv_reader:
                base, rates = row[0], row[1]
                cfg[base] = rates.split(' ')
                logging.info('Parsed base {} with rates for {}'.format(base, rates))
        logging.info('Parsed config file {}.'.format(cfg))
        return cfg

    # def _download_from_api(self):
    #     dl = []
    #     for base, to in self.cfg.items():
    #         response = HttpHook(method='GET', http_conn_id=self.conn_id).run(
    #             self.endpoint,
    #             data={
    #                 'base': base,
    #                 'symbols': ','.join(to)
    #             }
    #         )
    #         logging.info(response.text)
    #         dl.append(json.loads(response.text))
    #     return dl

    def dl_and_write(self, output_path, **context):
        dl = []
        for base, to in self.cfg.items():
            logging.info("Downloading symbols: {} converted to base: {}".format(','.join(to), base))
            response = HttpHook(method='GET', http_conn_id=self.conn_id).run(
                str(context['execution_date'].date()),
                data="base={}&symbols={}".format(base, ','.join(to))
            )
            logging.info(response.text)
            dl.append(json.loads(response.text))
        # turn into nice json and write
        logging.info("Writing to JSON file @ {}".format(output_path))
        with open(output_path, 'w') as f:
            json.dump({d['base']: d['rates'] for d in dl}, f)
