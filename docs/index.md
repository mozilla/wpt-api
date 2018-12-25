# Mozilla wpt-api Documentation
## (a.k.a Using WebPageTest...Mozilla Edition)

## Introduction
## Project Goals:
* Accurately measure, track, and report on key Firefox-performance metrics, over time
* Leverage, and be an integral part of, the [WebPageTest](https://www.webpagetest.org/) ecosystem

## High-Priority Needs:
### Metrics & timings/results' stability, repeatability
* Established/accepted baseline metrics; both 1) which ones, as well as 2) acceptable performance targets, benchmarks, budgets, etc.
* Standard Deviation for key metrics
* Easily-vetable and comparable runs

## Recommendations:
* We should **very** closely follow: https://w3c.github.io/performance-timeline/,<br>
which **would "enable web developers to access, instrument, and retrieve various performance metrics from the full lifecycle of a web application."**
* Continue soliciting workflows/use-cases from multiple teams, weighed with ongoing refinements/feature work
* Perhaps we should include output of ```window.performance.timing``` (to compare/contrast with ```WebPageTest``` -reported timing data)

## Metrics & Metadata:
### Current Status:
| Metric (units: raw + visualized) | To-Spec*? / Issues | Source / API | Calculation | WPT Config / Issues |
|:------------|:-------------|:-----|:-------|:------|
| ```bytesInDoc (count)``` | Y | ? | ? |  |
| ```DOMContentFlushed (N/A, sec)```| N; [Issue 97](https://github.com/mozilla/wpt-api/issues/97#issuecomment-432422829) -  needs calc. [PR pending](https://github.com/mozilla-services/cloudops-deployment/pull/2840/files) | Firefox-only; needs custom pref | ```timeToDOMContentFlushed``` ```-``` ```fetchStart``` | see ```timeToDOMContentFlushed```|
|[```fetchStart (ms/sec?)```](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/fetchStart) | N | N; [NavTiming API deprecated](https://w3c.github.io/navigation-timing/#obsolete) | ? | ? |
| [```firstPaint```](https://developer.mozilla.org/en-US/docs/Web/API/PerformancePaintTiming) | ? | ? | ? | ? |
| ```render (ms, sec)``` ([```startRender?```](https://sites.google.com/a/webpagetest.org/docs/using-webpagetest/quick-start-quide#TOC-Start-Render)) | ? | ? | Y | ? |
| ```requestsFull (count)``` | ? | ? | ? | n/a |
| [```SpeedIndex (integer, ?)```](https://sites.google.com/a/webpagetest.org/docs/using-webpagetest/metrics/speed-index) | Y  | WebPageTest-only | test-run-video analysis | ? |
| ```timeToDOMContentFlushed (ms, sec?)``` | Y | Firefox-only; needs custom pref <br>**-**<br>**Impl**: [bug 1457325](https://bugzilla.mozilla.org/show_bug.cgi?id=1457325)| ? | ```user_pref("dom.performance.time_to_dom_content_flushed.enabled", true)```in [wptagent/internal/support/Firefox/profile/prefs.js](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/support/Firefox/profile/prefs.js#L57)
| [```timeToConsistentlyInteractive (ms, sec?)```](https://github.com/WPO-Foundation/webpagetest/blob/c53214c24a99f52add146eba6aec1cd137a4bcee/docs/Metrics/TimeToInteractive.md#time-to-consistently-interactive-calculation) (```TTCI```) | N; pending-network requests | N;  | . | . | . |
| ```TTFB``` (```timeToFirstByte (ms)```) | Y | ? | ? | ? |
| ```timeToContentfulPaint (ms, sec?)``` / ```first contentful paint``` (```TT(F)CP``` / ```FCP```) | ? | <br>**-**<br>**Impl**. [bug 1298381](https://bugzilla.mozilla.org/show_bug.cgi?id=1298381) | ? | 
```user_pref("dom.performance.time_to_contentful_paint.enabled", true)``` in [wptagent/internal/support/Firefox/profile/prefs.js(https://github.com/WPO-Foundation/wptagent/pull/214/files#diff-463e288bcde710e9a9ef8a46d490aac1R58] and ```addTime("timeToContentfulPaint");``` in [wptagent/internal/js/page_data.js](https://github.com/WPO-Foundation/wptagent/pull/214/files#diff-69b0882d86377063fd0514c0dc978308R22)|
| [```timeToFirstNonBlankPaint (ms/sec?)```](https://bugzilla.mozilla.org/show_bug.cgi?id=1377251) (```TTFNBP?```) | ? |  Firefox-only; needs custom pref | ? | ```user_pref("dom.performance.time.to_non_blank_paint", true``` in [wptagent/internal/support/Firefox/profile/prefs.js](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/support/Firefox/profile/prefs.js#L60) |
|[```timeToFirstMeaningfulPaint (ms/sec?)```](https://developer.mozilla.org/en-US/docs/Web/API/PerformancePaintTiming) (```TTFMP```) | N | N; partial <br>**-**<br>**Impl**. [bug 1299117](https://bugzilla.mozilla.org/show_bug.cgi?id=1299117) | . | . |
| ```visualComplete (sec)``` (```timeToVisuallyComplete```) | Y | ? | ? | ? |
| ```browser_version``` (```string```) ```"61.0a"```| **n/a**; | . | . | ```self.marionette.session.capabilities``` in [wptagent/internal/firefox.py](https://github.com/WPO-Foundation/wptagent/blob/84018f548a2dea78dfca0ca64c19386adc6e2bca/internal/firefox.py#L128-L129)|

* "To-Spec?" is getting at: either/both:
  Metric implementation largely "matching" W3C / WHATWG, etc., (draft) specification/proposal/RFC...
  Mozilla and/or Chrome, WebPageTest, et al. general acceptance of a given metric, as-currently-is.  This might include early draft-spec feature branches, etc., 

### Manually Testing Metrics in Firefox
1. Enable/modify any (missing) prefs/pref-overrides
2. Open Tools -> Web Developer -> Web Console
3. Load a URL
4. After the page has "finished" loading, type something like: ```window.performance.timing.timeToFirstInteractive``` (**DO** take note of the other implemented/available metric options available as you autocomplete.)
5. Hit return/enter
6. You should see a value similar to ```1542438605479``` (time-stamped offset, in milliseconds) 

PRO-TIP: you can and *should* input ```window.performance.timing``` into the Console, to dump the entire PerformanceTiming object

**[XXX FIX ME - Upload a tantalizing screengrab, here]**

### Adding Metrics to WebPageTest with Firefox
1. Manually test the metric + pref (ahem); most metrics can be found in the following Firefox DOM WebIDL:  [```mozilla-central/dom/webidl/PerformanceTiming.webidl```](https://hg.mozilla.org/mozilla-central/file/tip/dom/webidl/PerformanceTiming.webidl)
2. If needed, add/modify Firefox's `prefs.js`, via a PR to  [```wptagent/internal/support/Firefox/profile/prefs.js```](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/support/Firefox/profile/prefs.js)
  Example: https://github.com/WPO-Foundation/wptagent/pull/181/files#diff-69b0882d86377063fd0514c0dc978308
3. Additionally, we might need to have the metric (if not available via standard APIs) emitted in WebPageTest, in [```wptagent/internal/js/page_data.js```](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/js/page_data.js#L27).

## WebPageTest Runs at Mozilla

This should be a mid-to-high level overview of pertinent Mozilla-specific goals, design considerations (challenges) and, as a brief overview, a visualization of our WPT ecosystem.

## Firefox-Pertinent *WPT* Code:
###  wptagent
* [```Dockerfile```](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/Dockerfile)
* [```desktop_browser.py```](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/desktop_browser.py) (base class for **_all_** browsers)
* [```browsers.py```](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/browsers.py) (self-described "Main entry point [sic] for controlling browsers")
* [```webpagetest.py```](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/webpagetest.py) (the one, the only)
* [```firefox.py```](https://github.com/WPO-Foundation/wptagent/blob/master/internal/firefox.py) (hey, that's us!)
* [```traffic-shaping.py```](https://github.com/WPO-Foundation/wptagent/blob/master/internal/traffic_shaping.py) (cross-platform rate-limiting, latency, etc. support)
* [```page_data.js```](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/js/page_data.js) (user timings, vendor-specific/internal metrics & configs/settings)
* [```firefox_log_parser.py```](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/support/firefox_log_parser.py) (where the metric-culling magic happens)
* [```visual_metrics.py```](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/support/visualmetrics.py) (the guts of the visual-comparison algorithms)
* [```trace_parser.py```](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/support/trace_parser.py) (calculates metrics with recipes/formulas)
* [```pcap_parser.py```](https://github.com/WPO-Foundation/wptagent/blob/3f2128a9815838f462187b870be3c666ebd13d95/internal/support/pcap-parser.py) (wait for it...parses pcap files!)

# Infrastructure
### WebPageTest Instance (*Mozilla-internal*)
* https://wpt.stage.mozaws.net - Auth0/OAuth
* https://wpt-api.stage.mozaws.net - Basic Auth
   * You'll need to file a bug in Cloud Ops, requesting access

### Jenkins
* [```https://qa-preprod-master.fxtest.jenkins.stage.mozaws.net/job/wpt/```](https://qa-preprod-master.fxtest.jenkins.stage.mozaws.net/job/wpt/)
   * To obtain access, see these (internal-only) [Mana docs](https://mana.mozilla.org/wiki/display/TestEngineering/qa-preprod-master.fxtest.jenkins.stage.mozaws.net)

### AWS EC2 Setup
* **1** ```c4.large``` __WebPageTest__ core server-instance (Linux, EC2 AMI ID: ami-024df0ababa7118ae)
* **4** x ```c5.xlarge``` __wptagent__ server instances (Linux, EC2 AMI ID: ami-a88c20d5)

## Dependencies
#### Core:
* [WebPageTest](https://github.com/WPO-Foundation/webpagetest/blob/master/README.md) (core/server)
* [wptagent](https://github.com/WPO-Foundation/wptagent/blob/master/README.md) (configs/runs browser tests, and collects and submits metrics/data to be post-processed by the above core WebPageTest server; the project formerly known as "wptdriver."
* [webpagetest-api](https://github.com/marcelduran/webpagetest-api/blob/master/README.md) (NodeJS-wrapped core API)

## W3C (Draft) Specs

* [Perf-Timing Primer](https://w3c.github.io/perf-timing-primer/)
* [Navigation Timing](https://www.w3.org/TR/navigation-timing/)
* [Navigation Timing Level 2](https://www.w3.org/TR/navigation-timing-2/) (Working Draft)
* [High-Resolution Time Level 2](https://www.w3.org/TR/hr-time-2/) 
* [Performance Timeline Level 2](https://www.w3.org/TR/performance-timeline-2/)
* [User Timing](https://www.w3.org/TR/user-timing/)

## Assorted Links:
* Example Mobile-Device Lab Config: https://github.com/WPO-Foundation/webpagetest-docs/blob/2db35b31fe1c992c02650a5b401f7ed208d8fa27/user/Private%20Instances/mobile/example.md
* https://www.w3.org/2000/09/dbwg/details?group=45211&order=org&public=1
* Web-platform tests we run: https://github.com/web-platform-tests/wpt/tree/744325921ba52791bc8db1b45d2aed097577753a/navigation-timing
***

## Contributions
***psst, this could be you!***

## Credits & Thanks
* Pat Meenan - too numerous to call out; thanks for the project, the community, the tooling, and your direct support
* Rick Viscomi, Andy Davies, & Marcel Duran - thanks for /the/ published book, and the numerous blog posts, Tweets, talks, forum posts, etc., to further its adoption/ecosystem
* Peter Hedenskog - for everything (he knows!)
* [Sitespeed.io crew](https://www.sitespeed.io/) - for helping me re-envision and prototype an idea from 2010!
* Wikimedia Performance Team for their [amazing + open WebPageTest setup](https://wikitech.wikimedia.org/wiki/Performance)
* Firefox Performance Team for their support & shared focus
