#!/usr/bin/env python3

from dataclasses import asdict, dataclass
import json
import sys

import requests


@dataclass
class TestResult:
    appName: str
    channel: str
    version: str
    url: str
    metrics: dict


def main(path):
    with open("wpt.json") as f:
        data = json.load(f)

    with open("metrics.json") as f:
        metrics = json.load(f)

    for test in data:
        sample = test["data"]["median"]["firstView"]
        values = {m["name"]: sample[m["name"]] for m in metrics}

        result = TestResult(
            appName=sample["browser_name"],
            channel="",
            version=sample["browser_version"],
            url=test["data"]["testUrl"],
            metrics=values)
        print(asdict(result))
        # print(json.dumps(asdict(result)))

        with open(f"wpt-telemetry-{test['data']['id']}.json", "w") as f:
            json.dump(asdict(result), f)

        # send to telemetry
        # r = requests.post(url="", data=asdict(result), type="json")
        # r.raise_on_error()


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python send_to_telemetry.py path")
        exit()
    main(*sys.argv[1:])
