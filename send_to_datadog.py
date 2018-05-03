from datadog import initialize, api
from datadog import statsd


options = {'statsd_host': 'localhost',
           'statsd_port': '8125'}

initialize(**options)

statsd.set('wpt.median.firstView.TTFB', '429')
