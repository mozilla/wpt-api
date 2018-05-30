import json

from datadog import initialize
from datadog import statsd


options = {'statsd_host': 'localhost',
           'statsd_port': '8125'}

with open('fxa-homepage.json') as json_data:
    loaded_json = json.load(json_data)

    '''
    Just leaving the example below, in, for my own reference
    print("data.median.firstView.TTFB {}".format(loaded_json["data"]["median"]["firstView"]["TTFB"]))
    '''


initialize(**options)

TTFB = loaded_json["data"]["median"]["firstView"]["TTFB"]
render = loaded_json["data"]["median"]["firstView"]["render"]
SpeedIndex = loaded_json["data"]["median"]["firstView"]["SpeedIndex"]
bytesInDoc = loaded_json["data"]["median"]["firstView"]["bytesInDoc"]
visualComplete = loaded_json["data"]["median"]["firstView"]["visualComplete"]
requestsFull = loaded_json["data"]["median"]["firstView"]["requestsFull"]

statsd.gauge('wpt.median.firstView.TTFB', (TTFB))
statsd.gauge('wpt.median.firstView.render', (render))
statsd.gauge('wpt.median.firstView.SpeedIndex', (SpeedIndex))
statsd.gauge('wpt.median.firstView.bytesInDoc', (bytesInDoc))
statsd.gauge('wpt.median.firstView.visualComplete', (visualComplete))
statsd.gauge('wpt.median.firstView.requestsFull', (requestsFull))
