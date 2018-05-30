[![Build Status](https://travis-ci.org/mozilla/wpt-api.svg?branch=master)](https://travis-ci.org/mozilla/wpt-api)

This repo aims to build a useful, versatile WebPagetest setup, which is both runnable out-of-the-box ready, and yet also configurable enough for multiple teams and use-cases.  Another explicit goal is to build off of and leverage existing solutions, where possible.

Currently implemented:

* Passing in a custom ```PAGE_URL``` to override the default
* Running tests against the URL with the following hardcoded parameters:
  - in the ```us-east-1``` EC2 region
  - 5 times
  - recent Firefox release
  - using ```--first``` (no caching)
* Post-run, we export and archive (via Jenkins) ```fxa-homepage.json```
* Next, using a Docker-run jq, we filter for and extract:
  - Time To First Byte
  - Start render
  - Speed Index
  - Total Bytes Transferred
  - Visually Complete time
  - Total # of Requests
* Next, we write out (and archive via Jenkins) a ```stats.json``` file

Eventually, and roughly in order of complexity and dependencies, we aim for:

* metrics/data submission/collection
  - via DogStatsD or a StatsD equivalent - [Issue 16](https://github.com/mozilla/wpt-api/issues/16)
* metrics/data plotting - [Issue 17](https://github.com/mozilla/wpt-api/issues/17)
* integration of perf metrics with code review (GitHub)/CI builds (TeamCity, Jenkins, Travis?), and post-deployment testing.
