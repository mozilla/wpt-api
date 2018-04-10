This repo aims to build a useful, versatile WebPagetest setup, which is both runnable out-of-the-box ready, and yet also configurable enough for multiple teams and use-cases.  Another explicit goal is to build off of and leverage existing solutions, where possible.

Docker was chosen to help make adoption, setup, and running WebPagetest easier and more portable, particularly in continuous-integration setups.

Eventually, and roughly in order of complexity and dependencies, we aim for:

* metrics/data submission/collection (app-agnostic)
* metrics/data plotting (app-agnostic)
* integration of perf metrics with code review (GitHub)/CI builds (TeamCity, Jenkins, Travis?), and post-deployment testing (app-agnostic).
