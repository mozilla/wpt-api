# wpt-api

[![license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/mozilla/wpt-api/blob/master/LICENSE.txt)
[![Build Status](https://travis-ci.org/mozilla/wpt-api.svg?branch=master)](https://travis-ci.org/mozilla/wpt-api)
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=mozilla/wpt-api)](https://dependabot.com)

This repo aims to build a useful, versatile WebPageTest setup, which is both out-of-the-box ready, and yet also configurable enough for multiple teams and use-cases.

Specifically, its primary aim is capturing, submitting, and visualizing web-performance metrics from a Firefox release build, run against the Firefox Accounts firstrun webpage.

The currently implemented workflow, on the ```master``` branch, supports:

* Passing in a custom ```PAGE_URL``` to override the hardcoded default[0]:
* Running tests against the URL with the following hardcoded parameters:
  - in the ```us-east-1-linux``` EC2 region
  - 5 times
  - recent Firefox release build, on Linux
  - using ```--first``` (no caching)
* Post-WebPageTest run, we export and archive its output (via Jenkins) as ```fxa-homepage.json```[1]
* Next, we filter for and extract[2]:
  - Time To First Byte (TTFB)
  - Time To Non-Blank Paint, aka ```firstPaint``` (firstPaint)
  - Start render (render)
  - Speed Index (SpeedIndex)
  - Total Bytes Transferred (bytesInDoc)
  - Visually Complete time (visualComplete)
  - Total # of Requests (requestsFull)
* Finally, the perf metrics are sent via a DataDog agent to its API[3], and are plotted, here (apologies; Mozilla-internal, for now - I'm working on opening it up):

https://app.datadoghq.com/dash/827265/firefox-accounts-dev-first-run-page-perf-metrics?live=true

![](https://user-images.githubusercontent.com/387249/43986821-0b5adddc-9ccc-11e8-924f-9d7420abc02a.png)

Eventually, and roughly in order of complexity and dependencies, we aim for:

* batch-URL/command processing
* integration of perf metrics with code review (GitHub)/CI builds (TeamCity, Jenkins, Travis?), and post-deployment testing

[0] https://github.com/mozilla/wpt-api/blob/13148b749268e1a1212042d8edb8731366bc2c4a/Jenkinsfile#L8<br/>
[1] https://github.com/mozilla/wpt-api/blob/13148b749268e1a1212042d8edb8731366bc2c4a/Jenkinsfile#L36-L43<br/>
[2] https://github.com/mozilla/wpt-api/blob/13148b749268e1a1212042d8edb8731366bc2c4a/send_to_datadog.py#L21-L26<br/>
[3] https://github.com/mozilla/wpt-api/blob/13148b749268e1a1212042d8edb8731366bc2c4a/send_to_datadog.py#L28-L33<br/>
