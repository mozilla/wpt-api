import json

from datadog import initialize
from datadog import statsd


options = {'statsd_host': 'localhost',
           'statsd_port': '8125'}

with open('alexa-topsites.json') as json_data:
    loaded_json = json.load(json_data)

    '''
    Just leaving the example below, in, for my own reference
    print("data.median.firstView.TTFB {}".format(loaded_json["data"]["median"]["firstView"]["TTFB"]))
    '''


initialize(**options)

test_names = ['google.fx.release', 'google.fx.nightly', 'google.chrome.release',
              'google.chrome.canary', 'youtube.fx.release', 'youtube.fx.nightly',
              'youtube.chrome.release', 'youtube.chrome.canary', 'facebook.fx.release',
              'facebook.fx.nightly', 'facebook.chrome.release', 'facebook.chrome.canary']
metrics = ['TTFB', 'render', 'firstPaint', 'timeToDOMContentFlushed', 'SpeedIndex', 'bytesInDoc',
           'visualComplete', 'requestsFull']

for test_name in test_names:
    for metric in metrics:
        statsd.gauge('wpt.batch.{}.median.firstView.{}'.format(test_name, metric),
                     loaded_json[test_names.index(test_name)]['data']['median']['firstView'][metric])
