from dataclasses import asdict, dataclass
import json
import os
import sys

# import requests


@dataclass
class TestResult:
    appName: str
    channel: str
    connection: str
    version: str
    url: str
    platform: str
    metrics: dict
    runner: str
    runId: str
    sessionState: str


def main(path):
    with open(path) as f:
        data = json.load(f)

    with open("metrics.json") as f:
        metrics = json.load(f)

    for test in data:
        build_tag = str(os.getenv("BUILD_TAG", "unknown"))
        print("BUILD_TAG is: ", build_tag)

        jenkins_URL = str(os.getenv("JENKINS_URL", "unknown"))
        print("JENKINS_URL is: ", jenkins_URL)

    for test in data:
        sample = test["data"]["median"]["firstView"]
        values = {"firstView": {}}

        for measure in ["median", "standardDeviation"]:
            values["firstView"][measure] = {}
            for metric in metrics:
                name = metric["name"]
                try:
                    value = test["data"][measure]["firstView"][name]
                    if value is not None:
                        values["firstView"][measure][name] = value
                except KeyError:
                    pass

        fullBrowserString = sample["browser_name"]
        print("Browser: ", fullBrowserString)

        browserName, _, channelName = sample["browser_name"].lower().partition(" ")
        channelName = channelName or "release"

        print("Channel: ", channelName)

        result = TestResult(
            appName=browserName,
            channel=channelName,
            connection=test["data"]["connectivity"].lower(),
            version=sample["browser_version"],
            url=test["data"]["testUrl"],
            platform="desktop",
            metrics=values,
            runner=jenkins_URL,
            runId=build_tag,
            sessionState="noAuth",
        )

        print(json.dumps(asdict(result)))
        # with open(f"wpt-telemetry-{test['data']['id']}.json", "w") as f:
        #   json.dump(asdict(result), f)

        # send to telemetry
        # r = requests.post(url="", data=asdict(result), type="json")
        # r.raise_on_error()


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python send_to_telemetry.py path")
        exit()
    main(*sys.argv[1:])
