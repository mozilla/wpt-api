# Mozilla wpt-api Documentation #

## Table of contents: ##

* [Introduction](#intro)
* [High-Priority Needs](#urgent)
* [Metrics](#metrics)
* [Firefox-Pertinent WPT Code](#wptFxCode)
* [Infrastructure](#infra)
* [Dependencies](#dependencies)
* [Contributions](#contributions)
* [Credits & Thanks](#credits)

## Introduction ##
## Project Goals ##
* Accurately measure, track, and report on key Firefox-performance metrics, over time
* Leverage, and be an integral part of, the WebPageTest ecosystem


## High-Priority Needs: ##
### Metrics & timings/results' stability, repeatability ###
* one
* two


## Metrics ##
|Metric|Visualized|Unit & Type|To-Spec|Computation & Source|Raptor|Bug|MDN|
| ------------- |:-------------:| -----:| -----:|-------:|-------:|-------:|-------:|
| ```bytesInDoc``` | Y |  | ? | n/a | N | n/a | n/a |
| ```DOMContentFlushed``` | N | ms; duration/offset | N; Firefox-only; needs custom pref | ```timeToDOMContentFlushed``` ```-``` ```fetchStart``` | N | n/a; see ```timeToDOMContentFlushed``` | n/a |
| ```fetchStart``` | N  | ms | N; [NavTiming API deprecated](https://w3c.github.io/navigation-timing/#obsolete) | ? | ? | . |   [ fetchStart](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/fetchStart) |
| ```firstPaint```  | Y  |  ?  | ? | ? | ? | ? | ? |      
| ```render``` (```startRender?```) | Y | sec or ms? | ? | Y | . |  . | . |
| ```requestsFull``` | Y | count |       | ? | n/a | . | . |
| ```SpeedIndex``` | Y  |  seconds |  N | test-run-video analysis | ? | . | . |
| ```timeToDOMContentFlushed``` | Y | ms since...? | N | gecko (?) | Y | [1457325](https://bugzilla.mozilla.org/show_bug.cgi?id=1457325)| . |
| ```TimeToConsistentlyInteractive``` (```TTCI```) | N | N; missing...? | . | . | . | . | . |
| ```TTFB``` (```timeToFirstByte```) | Y | ms | ? | wpt algo? | ? | n/a | n/a  
| ```TimeToFirstContentfulPaint``` (```TTFCP```) |  N | ms | . | . | . | Impl. in [bug 1298381](https://bugzilla.mozilla.org/show_bug.cgi?id=1298381) | . |
| ```TimeToFirstMeaningfulPaint``` (```TMP```) | ? | ms | N; partial | . | . | . |
| ```visualComplete``` (```timeToVisuallyComplete```) | Y | seconds | . | . | . | . | . |

"Standard" used here to denote, for a given metric:
* We consider said metric to be implemented consistently (throughout the entire test-run & reporting workflow) and in close adherence with a corresponding [Navigation Timing, Performance Timing, PerformanceNavigationTiming, User Timing, et al ] Timing API specification.

## Firefox-Pertinent WPT Code ##
###  wptagent ###
* ```Dockerfile```
* ```desktop_browser.py``` (base class for **_all_** browsers)
* ```browsers.py``` (self-described "Main entry point [sic] for controlling browsers")
* ```webpagetest.py``` (the one, the only)
* ```firefox.py``` (hey, that's us!) -->
[**code**](https://github.com/WPO-Foundation/wptagent/blob/master/internal/firefox.py)
* ```traffic-shaping.py``` (cross-platform rate-limiting, latency, etc. support) -->
[**code**](https://github.com/WPO-Foundation/wptagent/blob/master/internal/traffic_shaping.py)
* ```page_data.js``` (user timings, vendor-specific/internal metrics & configs/settings)
* ```firefox_log_parser.py``` (where the metric-culling magic happens)
* ```visual_metrics.py``` (the guts of the visual-comparison algorithms)
* ```trace_parser.py``` (calculates metrics with recipes/formulas)
* ```pcap_parser.py``` (wait for it...parses pcap files!)

## Infrastructure ##

### WebPageTest Instance (*Mozilla-internal*) ###
* https://wpt.stage.mozaws.net - Auth0/OAuth
* https://wpt-api.stage.mozaws.net - Basic Auth

### Jenkins ###
* https://qa-preprod-master.fxtest.jenkins.stage.mozaws.net/job/wpt/ - [Docs](https://mana.mozilla.org/wiki/display/TestEngineering/qa-preprod-master.fxtest.jenkins.stage.mozaws.net) (in Mana)

### AWS EC2 Setup ###
* 1 ```c4.large``` __WebPageTest__ core server-instance (Linux, EC2 AMI ID: XXX)
* 4 **x** ```c5.xlarge``` __wptagent__ server instances (Linux, EC2 AMI ID: XXX)


## Dependencies ##
#### Core: ####
* [WebPageTest](https://github.com/WPO-Foundation/webpagetest/blob/master/README.md) (core/server)
* [wptagent](https://github.com/WPO-Foundation/wptagent/blob/master/README.md)
* [webpagetest-api](https://github.com/marcelduran/webpagetest-api/blob/master/README.md)

## Contributions ##
## Credits & Fist-bumps ##
* Pat Meenan
* Rick Viscomi, Andy Davies, & Marcel Duran
* Peter Hedenskog
* Wikimedia Performance Team
* Firefox Performance Team
