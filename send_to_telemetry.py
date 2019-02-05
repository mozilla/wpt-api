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
    with open("wpt.json") as f:
        data = json.load(f)

    with open("metrics.json") as f:
        metrics = json.load(f)

    for test in data:
        build_tag = str(os.environ['BUILD_TAG'])
        print("BUILD_TAG is: ", build_tag)

        print("                                     ")

        jenkins_URL = str(os.environ['JENKINS_URL'])
        print("JENKINS_URL is: ", jenkins_URL)
        print("                                     ")


        standardDeviation = test["data"]["standardDeviation"]["firstView"]
        print ("Standard deviation: ", standardDeviation.items())
        # print(standardDeviation)
        # print("Standard Deviation objects", standardDeviation)

        medianMetric = test["data"]["median"]["firstView"]
        print ("Median metric: ", medianMetric.items())
        # print(medianMetric)
        # print("Median metric objects", medianMetric)
        # print(medianMetric)
        # print("==========================")

    for test in data:
        sample = test["data"]["median"]["firstView"]
        values = {m["name"]: sample[m["name"]] for m in metrics}

        fullBrowserString = sample["browser_name"]
        print("                                     ")
        print("Browser: ", fullBrowserString)

        # need to only partition if we have a space in fullBrowserString, e.g. "Firefox Nightly"
        if ' ' in fullBrowserString:
            splitBrowserStrings = fullBrowserString.partition(' ')
            uppercaseBrowserName = splitBrowserStrings[0]
            lowercaseBrowserName = splitBrowserStrings[0].lower()
            browserName = lowercaseBrowserName
        else:
            browserName = fullBrowserString.lower()

        # construct 'channel'
        if ' ' in fullBrowserString:
            channelName = splitBrowserStrings[2].lower()
        else:
            channelName = 'release'

        print("Channel: ", channelName)

        result = TestResult(
            appName=browserName.lower(),
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
