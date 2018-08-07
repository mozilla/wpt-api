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

TTFB_google_fx_release = loaded_json[0]["data"]["median"]["firstView"]["TTFB"]
render_google_fx_release = loaded_json[0]["data"]["median"]["firstView"]["render"]
timeToNonBlankPaint_google_fx_release = loaded_json["data"]["median"]["firstView"]["firstPaint"]
SpeedIndex_google_fx_release = loaded_json[0]["data"]["median"]["firstView"]["SpeedIndex"]
bytesInDoc_google_fx_release = loaded_json[0]["data"]["median"]["firstView"]["bytesInDoc"]
visualComplete_google_fx_release = loaded_json[0]["data"]["median"]["firstView"]["visualComplete"]
requestsFull_google_fx_release = loaded_json[0]["data"]["median"]["firstView"]["requestsFull"]

statsd.gauge('wpt.batch.google.fx.release.median.firstView.TTFB', (TTFB_google_fx_release))
statsd.gauge('wpt.batch.google.fx.release.median.firstView.render', (render_google_fx_release))
statsd.gauge('wpt.batch.google.fx.release.median.firstView.firstPaint', (timeToNonBlankPaint_google_fx_release))
statsd.gauge('wpt.batch.google.fx.release.median.firstView.SpeedIndex', (SpeedIndex_google_fx_release))
statsd.gauge('wpt.batch.google.fx.release.median.firstView.bytesInDoc', (bytesInDoc_google_fx_release))
statsd.gauge('wpt.batch.google.fx.release.median.firstView.visualComplete', (visualComplete_google_fx_release))
statsd.gauge('wpt.batch.google.fx.release.median.firstView.requestsFull', (requestsFull_google_fx_release))


TTFB_google_fx_nightly = loaded_json[1]["data"]["median"]["firstView"]["TTFB"]
render_google_fx_nightly = loaded_json[1]["data"]["median"]["firstView"]["render"]
timeToNonBlankPaint_google_fx_nightly = loaded_json["data"]["median"]["firstView"]["firstPaint"]
SpeedIndex_google_fx_nightly = loaded_json[1]["data"]["median"]["firstView"]["SpeedIndex"]
bytesInDoc_google_fx_nightly = loaded_json[1]["data"]["median"]["firstView"]["bytesInDoc"]
visualComplete_google_fx_nightly = loaded_json[1]["data"]["median"]["firstView"]["visualComplete"]
requestsFull_google_fx_nightly = loaded_json[1]["data"]["median"]["firstView"]["requestsFull"]

statsd.gauge('wpt.batch.google.fx.nightly.median.firstView.TTFB', (TTFB_google_fx_nightly))
statsd.gauge('wpt.batch.google.fx.nightly.median.firstView.render', (render_google_fx_nightly))
statsd.gauge('wpt.batch.google.fx.nightly.median.firstView.firstPaint', (timeToNonBlankPaint_google_fx_nightly))
statsd.gauge('wpt.batch.google.fx.nightly.median.firstView.SpeedIndex', (SpeedIndex_google_fx_nightly))
statsd.gauge('wpt.batch.google.fx.nightly.median.firstView.bytesInDoc', (bytesInDoc_google_fx_nightly))
statsd.gauge('wpt.batch.google.fx.nightly.median.firstView.visualComplete', (visualComplete_google_fx_nightly))
statsd.gauge('wpt.batch.google.fx.nightly.median.firstView.requestsFull', (requestsFull_google_fx_nightly))

TTFB_google_chrome_release = loaded_json[2]["data"]["median"]["firstView"]["TTFB"]
render_google_chrome_release = loaded_json[2]["data"]["median"]["firstView"]["render"]
timeToNonBlankPaint_google_chrome_release = loaded_json["data"]["median"]["firstView"]["firstPaint"]
SpeedIndex_google_chrome_release = loaded_json[2]["data"]["median"]["firstView"]["SpeedIndex"]
bytesInDoc_google_chrome_release = loaded_json[2]["data"]["median"]["firstView"]["bytesInDoc"]
visualComplete_google_chrome_release = loaded_json[2]["data"]["median"]["firstView"]["visualComplete"]
requestsFull_google_chrome_release = loaded_json[2]["data"]["median"]["firstView"]["requestsFull"]

statsd.gauge('wpt.batch.google.chrome.release.median.firstView.TTFB', (TTFB_google_chrome_release))
statsd.gauge('wpt.batch.google.chrome.release.median.firstView.render', (render_google_chrome_release))
statsd.gauge('wpt.batch.google.chrome.release.median.firstView.firstPaint', (timeToNonBlankPaint_google_chrome_release))
statsd.gauge('wpt.batch.google.chrome.release.median.firstView.SpeedIndex', (SpeedIndex_google_chrome_release))
statsd.gauge('wpt.batch.google.chrome.release.median.firstView.bytesInDoc', (bytesInDoc_google_chrome_release))
statsd.gauge('wpt.batch.google.chrome.release.median.firstView.visualComplete', (visualComplete_google_chrome_release))
statsd.gauge('wpt.batch.google.chrome.release.median.firstView.requestsFull', (requestsFull_google_chrome_release))

TTFB_youtube_fx_release = loaded_json[3]["data"]["median"]["firstView"]["TTFB"]
render_youtube_fx_release = loaded_json[3]["data"]["median"]["firstView"]["render"]
timeToNonBlankPaint_youtube_fx_release = loaded_json["data"]["median"]["firstView"]["firstPaint"]
SpeedIndex_youtube_fx_release = loaded_json[3]["data"]["median"]["firstView"]["SpeedIndex"]
bytesInDoc_youtube_fx_release = loaded_json[3]["data"]["median"]["firstView"]["bytesInDoc"]
visualComplete_youtube_fx_release = loaded_json[3]["data"]["median"]["firstView"]["visualComplete"]
requestsFull_youtube_fx_release = loaded_json[3]["data"]["median"]["firstView"]["requestsFull"]

statsd.gauge('wpt.batch.youtube.fx.release.median.firstView.TTFB', (TTFB_youtube_fx_release))
statsd.gauge('wpt.batch.youtube.fx.release.median.firstView.render', (render_youtube_fx_release))
statsd.gauge('wpt.batch.youtube.fx.release.median.firstView.firstPaint', (timeToNonBlankPaint_youtube_fx_release))
statsd.gauge('wpt.batch.youtube.fx.release.median.firstView.SpeedIndex', (SpeedIndex_youtube_fx_release))
statsd.gauge('wpt.batch.youtube.fx.release.median.firstView.bytesInDoc', (bytesInDoc_youtube_fx_release))
statsd.gauge('wpt.batch.youtube.fx.release.median.firstView.visualComplete', (visualComplete_youtube_fx_release))
statsd.gauge('wpt.batch.youtube.fx.release.median.firstView.requestsFull', (requestsFull_youtube_fx_release))

TTFB_youtube_fx_nightly = loaded_json[4]["data"]["median"]["firstView"]["TTFB"]
render_youtube_fx_nightly = loaded_json[4]["data"]["median"]["firstView"]["render"]
timeToNonBlankPaint_youtube_fx_nightly = loaded_json["data"]["median"]["firstView"]["firstPaint"]
SpeedIndex_youtube_fx_nightly = loaded_json[4]["data"]["median"]["firstView"]["SpeedIndex"]
bytesInDoc_youtube_fx_nightly = loaded_json[4]["data"]["median"]["firstView"]["bytesInDoc"]
visualComplete_youtube_fx_nightly = loaded_json[4]["data"]["median"]["firstView"]["visualComplete"]
requestsFull_youtube_fx_nightly = loaded_json[4]["data"]["median"]["firstView"]["requestsFull"]

statsd.gauge('wpt.batch.youtube.fx.nightly.median.firstView.TTFB', (TTFB_youtube_fx_nightly))
statsd.gauge('wpt.batch.youtube.fx.nightly.median.firstView.render', (render_youtube_fx_nightly))
statsd.gauge('wpt.batch.youtube.fx.nightly.median.firstView.firstPaint', (timeToNonBlankPaint_youtube_fx_nightly))
statsd.gauge('wpt.batch.youtube.fx.nightly.median.firstView.SpeedIndex', (SpeedIndex_youtube_fx_nightly))
statsd.gauge('wpt.batch.youtube.fx.nightly.median.firstView.bytesInDoc', (bytesInDoc_youtube_fx_nightly))
statsd.gauge('wpt.batch.youtube.fx.nightly.median.firstView.visualComplete', (visualComplete_youtube_fx_nightly))
statsd.gauge('wpt.batch.youtube.fx.nightly.median.firstView.requestsFull', (requestsFull_youtube_fx_nightly))

TTFB_youtube_chrome_release = loaded_json[5]["data"]["median"]["firstView"]["TTFB"]
render_youtube_chrome_release = loaded_json[5]["data"]["median"]["firstView"]["render"]
timeToNonBlankPaint_youtube_chrome_release = loaded_json[5]["data"]["median"]["firstView"]["render"]
SpeedIndex_youtube_chrome_release = loaded_json[5]["data"]["median"]["firstView"]["SpeedIndex"]
bytesInDoc_youtube_chrome_release = loaded_json[5]["data"]["median"]["firstView"]["bytesInDoc"]
visualComplete_youtube_chrome_release = loaded_json[5]["data"]["median"]["firstView"]["visualComplete"]
requestsFull_youtube_chrome_release = loaded_json[5]["data"]["median"]["firstView"]["requestsFull"]

statsd.gauge('wpt.batch.youtube.chrome.release.median.firstView.TTFB', (TTFB_youtube_chrome_release))
statsd.gauge('wpt.batch.youtube.chrome.release.median.firstView.render', (render_youtube_chrome_release))
statsd.gauge('wpt.batch.youtube.chrome.release.median.firstView.firstPaint', (timeToNonBlankPaint_youtube_chrome_release))
statsd.gauge('wpt.batch.youtube.chrome.release.median.firstView.SpeedIndex', (SpeedIndex_youtube_chrome_release))
statsd.gauge('wpt.batch.youtube.chrome.release.median.firstView.bytesInDoc', (bytesInDoc_youtube_chrome_release))
statsd.gauge('wpt.batch.youtube.chrome.release.median.firstView.visualComplete', (visualComplete_youtube_chrome_release))
statsd.gauge('wpt.batch.youtube.chrome.release.median.firstView.requestsFull', (requestsFull_youtube_chrome_release))
