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

TTFB_chrome = loaded_json[0]["data"]["median"]["firstView"]["TTFB"]
render_chrome = loaded_json[0]["data"]["median"]["firstView"]["render"]
SpeedIndex_chrome = loaded_json[0]["data"]["median"]["firstView"]["SpeedIndex"]
bytesInDoc_chrome = loaded_json[0]["data"]["median"]["firstView"]["bytesInDoc"]
visualComplete_chrome = loaded_json[0]["data"]["median"]["firstView"]["visualComplete"]
requestsFull_chrome = loaded_json[0]["data"]["median"]["firstView"]["requestsFull"]

statsd.gauge('wpt.batch.chrome.median.firstView.TTFB', (TTFB_chrome))
statsd.gauge('wpt.batch.chrome.median.firstView.render', (render_chrome))
statsd.gauge('wpt.batch.chrome.median.firstView.SpeedIndex', (SpeedIndex_chrome))
statsd.gauge('wpt.batch.chrome.median.firstView.bytesInDoc', (bytesInDoc_chrome))
statsd.gauge('wpt.batch.chrome.median.firstView.visualComplete', (visualComplete_chrome))
statsd.gauge('wpt.batch.chrome.median.firstView.requestsFull', (requestsFull_chrome))

TTFB_firefox = loaded_json[1]["data"]["median"]["firstView"]["TTFB"]
render_firefox = loaded_json[1]["data"]["median"]["firstView"]["render"]
SpeedIndex_firefox = loaded_json[1]["data"]["median"]["firstView"]["SpeedIndex"]
bytesInDoc_firefox = loaded_json[1]["data"]["median"]["firstView"]["bytesInDoc"]
visualComplete_firefox = loaded_json[1]["data"]["median"]["firstView"]["visualComplete"]
requestsFull_firefox = loaded_json[1]["data"]["median"]["firstView"]["requestsFull"]

statsd.gauge('wpt.batch.firefox.median.firstView.TTFB', (TTFB_firefox))
statsd.gauge('wpt.batch.firefox.median.firstView.render', (render_firefox))
statsd.gauge('wpt.batch.firefox.median.firstView.SpeedIndex', (SpeedIndex_firefox))
statsd.gauge('wpt.batch.firefox.median.firstView.bytesInDoc', (bytesInDoc_firefox))
statsd.gauge('wpt.batch.firefox.median.firstView.visualComplete', (visualComplete_firefox))
statsd.gauge('wpt.batch.firefox.median.firstView.requestsFull', (requestsFull_firefox))
