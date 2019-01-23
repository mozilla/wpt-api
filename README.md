# Mozilla wpt-api

[![license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/mozilla/wpt-api/blob/master/LICENSE.txt)
[![Documentation Status](https://readthedocs.org/projects/mozilla-wpt-api-docs/badge/?version=master)](https://mozilla-wpt-api-docs.readthedocs.io/en/master/?badge=master)
[![Build Status](https://travis-ci.org/mozilla/wpt-api.svg?branch=master)](https://travis-ci.org/mozilla/wpt-api)
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=mozilla/wpt-api)](https://dependabot.com)

Using [Pat Meenan's](https://twitter.com/patmeenan) amazing [WebPageTest](https://www.webpagetest.org/) with [Marcel Duran's](https://twitter.com/marcelduran) super-handy NodeJS wrapper API in [webpagetest-api](https://github.com/marcelduran/webpagetest-api), this project tests, captures, submits, and visualizes key Web-performance metrics for a **_modified_** [Alexa top 50 sites list](https://github.com/mozilla/wpt-api/blob/master/top50.json) using Firefox "Quantum" release and Nightly desktop builds, and Google Chrome release and Canary (Nightly) builds, all on Linux (Ubuntu 18.04 LTS).

Special thanks to [Peter Hedenskog](https://www.peterhedenskog.com/) and the entire [Wikimedia Performance team](https://www.mediawiki.org/wiki/Wikimedia_Performance_Team) for getting me (and many others!) started and seeing me through, all the way here.

Stack: AWS (EC2 AMIs), Docker, Jenkins (Declarative Pipeline), Python, JavaScript

![](https://user-images.githubusercontent.com/387249/50874523-238e2700-1379-11e9-8835-058b4541aabc.png)

## Resources ##
* [Documentation](https://mozilla-wpt-api-docs.readthedocs.io/en/master/)
* [Issue Tracker](https://github.com/mozilla/wpt-api/issues)
* [Source Code](https://github.com/mozilla/wpt-api)
