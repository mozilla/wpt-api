import json

from datadog import initialize, api
from datadog import statsd


options = {'statsd_host': 'localhost',
           'statsd_port': '8125'}

with open ('fxa-homepage.json') as json_data:
    loaded_json = json.load(json_data)
    # dumped_json = json.dumps(loaded_json)
    # print(dumped_json)
    print "data.median.firstView.TTFB {}".format(loaded_json["data"]["median"]["firstView"]["TTFB"])
    print "data.median.firstView.render {}".format(loaded_json["data"]["median"]["firstView"]["render"])
    print "data.median.firstView.SpeedIndex {}".format(loaded_json["data"]["median"]["firstView"]["SpeedIndex"])
    print "data.median.firstView.bytesInDoc {}".format(loaded_json["data"]["median"]["firstView"]["bytesInDoc"])
    print "data.median.firstView.visualComplete {}".format(loaded_json["data"]["median"]["firstView"]["visualComplete"])
    print "data.median.firstView.requestsFull {}".format(loaded_json["data"]["median"]["firstView"]["requestsFull"])

print('wpt.median.firstView.TTFB', '{}'.format(loaded_json["data"]["median"]["firstView"]["TTFB"]))


initialize(**options)

# statsd.gauge('wpt.median.firstView.TTFB.fakeValue', '42', sample_rate=1)
# statsd.gauge('wpt.median.firstView.TTFB', loaded_json["data"]["median"]["firstView"]["TTFB"], sample_rate=1)

self.gauge('wpt.median.firstView.TTFB.fakeValue', '42', sample_rate=1)

# statsd.set('wpt.median.firstView.TTFB.fakeValue', '42')
# statsd.set('wpt.median.firstView.TTFB', loaded_json["data"]["median"]["firstView"]["TTFB"])
