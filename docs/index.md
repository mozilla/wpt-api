# Mozilla wpt-api Documentation

Welcome/preamble/elevator pitch

Guiding principle: test what we ship

## Table of contents:

* [Introduction](#intro)
* [Perf Metrics](#metrics)
* [Infrastructure](#infra)
* [Dependencies](#dependencies)
* [Contribute](#contribute)
* [Credits & Thanks](#credits)

## Introduction

Lorem

## Metrics
| Metric        | Visualized    | Metric Unit (In) |(Rec/Draft+) Standard* | Computation/Derivation | In Raptor | Bug(s) | MDN |
| ------------- |:-------------:| -----:| -----:|-------:|-------:|-------:|-------:|
| ```bytesInDoc``` | Y |  | ? | n/a | N | n/a | n/a |
| ```DOMContentFlushed``` | N | ms; duration/offset | N; Firefox-only; needs custom pref | ```timeToDOMContentFlushed``` ```-``` ```fetchStart``` | N | n/a; see ```timeToDOMContentFlushed``` | n/a |
| ```fetchStart``` | N  | ms | N; API deprecated | ? | ? | . |   [ fetchStart](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/fetchStart) |
| ```firstPaint```  | Y  |  ?  | ? | ? | ? | ? | ? |      
| ```render``` (```startRender?```) | Y | sec or ms? | ? | Y | . |  . | . |
| ```requestsFull``` | Y | count |       | ? | n/a | . | . |
| ```SpeedIndex``` | Y  |  seconds |  N | test-run-video analysis | ? | . | . |
| ```timeToDOMContentFlushed``` | Y | ms since...? | N | gecko (?) | Y | [1457325](https://bugzilla.mozilla.org/show_bug.cgi?id=1457325)| . |
| ```TimeToConsistentlyInteractive``` (```TTCI```) | N | N; missing...? | . | . | . | . | . |
| ```TTFB``` (```timeToFirstByte```) | Y | ms | ? | wpt algo? | ? | n/a | n/a  
| ```TimeToFirstContentfulPaint``` (```TTFCP)``` |  N | ms | . | . | . | [1298381](https://bugzilla.mozilla.org/show_bug.cgi?id=1298381) | . |
| ```visualComplete``` | Y | seconds | . | . | . | . | . |

"Standard" used here to denote, for a given metric:
* We consider said metric to be implemented consistently (throughout the entire test-run & reporting workflow) and in close adherence with a corresponding [Navigation Timing, Performance Timing, PerformanceNavigationTiming, User Timing, et al ] Timing API specification.

### Infrastructure ###

#### WebPageTest Instance (Mozilla-internal) ####
* Auth0/OAuth
* Basic Auth

#### Jenkins ####

### Dependencies ###
#### Core: ###
* WebPageTest (core/server)
* wptagent
* webpagetest-api

  webpagetest-api


#### Contribute

Sit

##### Credits & Thanks
