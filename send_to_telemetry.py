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

        # browser_names we need to support:
        # "Firefox Nightly"
        # "Firefox"
        # "Chrome"
        # "Chrome Canary"

        fullBrowserName = sample["browser_name"]
        print("Full browser name", fullBrowserName)
        lowercaseBrowser = fullBrowserName.lower()
        print("Lowercase browser name", lowercaseBrowser)
        splitBrowserName = fullBrowserName.partition(' ')
        print("Paritioned browser_name string", splitBrowserName)
        appName = fullBrowserName[0]
        if fullBrowserName[2]:
            channel = fullBrowserName[2]

        else
            channel = 'release'

        print(fullBrowserName)
        print(channel)
        print(fullBrowserName[0], fullBrowserName[1], fullBrowserName[2])


        # 1. partition string on space ' '
        # 2. call lower() on fullBrowserName[0]
        # 3. set appName=fullBrowserName[0]

        result = TestResult(
            appName = fullBrowserName[0],
            # appName=sample["browser_name"],

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
