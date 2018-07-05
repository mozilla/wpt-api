import json

from datadog import initialize
from datadog import statsd


options = {'statsd_host': 'localhost',
           'statsd_port': '8125'}

with open('batch-URL-results.json') as json_data:
    loaded_json = json.load(json_data)

    '''
    Just leaving the example below, in, for my own reference
    print("data.median.firstView.TTFB {}".format(loaded_json["data"]["median"]["firstView"]["TTFB"]))
    '''


initialize(**options)


TTFB_firefox = loaded_json["data"]["median"]["firstView"]["TTFB"]
render_firefox = loaded_json["data"]["median"]["firstView"]["render"]
SpeedIndex_firefox = loaded_json["data"]["median"]["firstView"]["SpeedIndex"]
bytesInDoc_firefox = loaded_json["data"]["median"]["firstView"]["bytesInDoc"]
visualComplete_firefox = loaded_json["data"]["median"]["firstView"]["visualComplete"]
requestsFull_firefox = loaded_json["data"]["median"]["firstView"]["requestsFull"]

statsd.gauge('wpt.batch.firefox.median.firstView.TTFB', (TTFB_firefox))
statsd.gauge('wpt.batch.firefox.median.firstView.render', (render_firefox))
statsd.gauge('wpt.batch.firefox.median.firstView.SpeedIndex', (SpeedIndex_firefox))
statsd.gauge('wpt.batch.firefox.median.firstView.bytesInDoc', (bytesInDoc_firefox))
statsd.gauge('wpt.batch.firefox.median.firstView.visualComplete', (visualComplete_firefox))
statsd.gauge('wpt.batch.firefox.median.firstView.requestsFull', (requestsFull_firefox))
