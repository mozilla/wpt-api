# wpt-api

[![license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/mozilla/wpt-api/blob/master/LICENSE.txt)
[![Build Status](https://travis-ci.org/mozilla/wpt-api.svg?branch=master)](https://travis-ci.org/mozilla/wpt-api)
[![Updates](https://pyup.io/repos/github/mozilla/wpt-api/shield.svg)](https://pyup.io/repos/github/mozilla/wpt-api/)
[![Python 3](https://pyup.io/repos/github/mozilla/wpt-api/python-3-shield.svg)](https://pyup.io/repos/github/mozilla/wpt-api/)

This repo's branch aims to capture, submit, and visualizing web-performance metrics for the Alexa top 3 sites, using Firefox Quantum release and Nightly builds, and Google Chrome, all on Linux.

The currently implemented setup, on the ```alexa-topsites``` branch, supports this workflow:

1. Passing in the top three (3) Alexa topsites' URLs (without scheme)
1. Running tests against those URLs with the following hardcoded parameters:
  - -l (location) in the ```us-east-1-linux``` EC2 region
  - -r (# of runs) 5
  - browsers:
  * latest Firefox Quantum release build, on Linux
  * latest Firefox Nightly build, on Linux
  * latest Google Chrome build, on Linux
  - using ```--first``` (no caching)
1. Post-WebPageTest run, we export and archive its output (via Jenkins) as ```alexa-topsites.json```[0]
1. Next, we filter for and extract the following performance-timing metrics[1]:
  - Time To First Byte (TTFB)
  - Time To First Non-Blank Paint, aka ```firstPaint``` (firstPaint)
  - Start render (render)
  - Speed Index (SpeedIndex)
  - Total # of Bytes Transferred (bytesInDoc)
  - Time to Visually Complete (visualComplete)
  - Total # of Requests (requestsFull)
1. Finally, the perf metrics are sent via a DataDog agent to its API[2], and are plotted, here:

https://app.datadoghq.com/dash/879449

--

[0] https://github.com/mozilla/wpt-api/blob/52c23959d7ed7196fcacf3ea5c61125e5a37bceb/Jenkinsfile#L29-L37<br/>
[1] https://github.com/mozilla/wpt-api/blob/52c23959d7ed7196fcacf3ea5c61125e5a37bceb/send_to_datadog.py#L21-L31<br/>
[2] https://github.com/mozilla/wpt-api/blob/52c23959d7ed7196fcacf3ea5c61125e5a37bceb/send_to_datadog.py#L30<br/>
