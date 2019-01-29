from dataclasses import asdict, dataclass
import json
import sys

# import requests


@dataclass
class TestResult:
    appName: str
    channel: str
    connection: str
    url: str
    platform: str
    runner: str
    runId: str
    metrics: dict
    sessionState: str
    version: str


def main(path):
    with open("wpt.json") as f:
        data = json.load(f)

    with open("metrics.json") as f:
        metrics = json.load(f)

    for test in data:
        sample = test["data"]["median"]["firstView"]
        values = {m["name"]: sample[m["name"]] for m in metrics}

        fullBrowserString = sample["browser_name"]
        print("Full browser name and (potentially) channel (hence fullBrowserString) is: ", fullBrowserString)
        print("Should be one of: 'Firefox', 'Firefox Nightly', 'Chrome', or 'Chrome Canary'")

        # need to only partition if we have a space in fullBrowserString
        if " " in fullBrowserString:
            splitBrowserStrings = fullBrowserString.partition(" ")
            uppercaseBrowserName = splitBrowserStrings[0]
            print("Partitioned browser_name string (splitBrowserStrings) is: ", splitBrowserStrings[0])
            lowercaseBrowserName = splitBrowserStrings[0].lower()
            print("Lowercase browser strings: (lowercaseBrowserStrings) is: ", lowercaseBrowserStrings)
            browserName = lowercaseBrowserName
        else:
            browserName = sample["browser_name"]

        # construct 'channel'
        print("Try to set 'channel', using lowercaseBrowserStrings")
        if lowercaseBrowserStrings[2]:
            channelName = lowercaseBrowserStrings[2]
        else:
            channelName = 'release'

        result = TestResult(
            appName = browserName,
            # appName=sample["browser_name"],
            channel=channelName,
            connection=test["data"]["connectivity"],
            url=test["data"]["testUrl"],
            platform="desktop",
            runner="",
            runId=test["data"]["id"],
            sessionState="noAuth",
            metrics=values,
            version=sample["browser_version"])
        # print(asdict(result))
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
