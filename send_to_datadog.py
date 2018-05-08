import json

from datadog import initialize, api
from datadog import statsd


options = {'statsd_host': 'localhost',
           'statsd_port': '8125'}

with open ('stats.json') as json_data:
    statsd_data = json.load(json_data)
    print(statsd_data)

initialize(**options)

statsd.gauge(statsd_data)
