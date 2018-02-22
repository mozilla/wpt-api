This repo will hopefully be useful in helping to stand up a versatile WebPagetest setup, in the primary context of performance-testing FxA (API/middleware/backend server, etc.) As an ancillary goal, we should strive to help make the setup easily adaptable for use by other teams.

Eventually, and roughly in order of complexity and dependencies, we aim for:

* metrics/data submission/collection (app-agnostic)
* metrics/data plotting (app-agnostic)
* a shared understanding of baseline performance (specific to FxA)
* integration of perf metrics with code review (GitHub)/CI builds (TeamCity, Jenkins, Travis?), and post-deployment testing (app-agnostic).
