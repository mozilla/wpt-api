from dataclasses import asdict, dataclass
import json
import os
import sys
import uuid

from jsonschema import validate

import requests


@dataclass
class TestResult:
    appName: str
    channel: str
    version: str
    connection: str
    url: str
    platform: str
    runner: str
    runId: str
    sessionState: str
    metrics: dict


def main(path):
    with open(path) as f:
        data = json.load(f)

    with open("metrics.json") as f:
        metrics = json.load(f)

    for test in data:
        # create an empty dictionary
        values = {}
        # grab each metric from metrics.json
        for metric in metrics:
            name = metric["name"]
            # now, grab all metrics' values
            for measure in ["median", "standardDeviation"]:
                sample = test["data"][measure]["firstView"].get(name)
                # sefdefault() will return each metric value
                # or, if missing, return and set an empty dict
                # if we find a metric in the dict, set its value
                # in the values{} dict
                if sample is not None:
                    m = values.setdefault(name, {})
                    # if the metric has a "firstView" entry + value,
                    # happily write it into values{}
                    # or, if missing, return and set an empty dict
                    first_view = m.setdefault("firstView", {})
                    first_view[measure] = sample

        sample = test["data"]["median"]["firstView"]
        # get browser name and channel, then lower()-case them
        browser, _, channel = sample["browser_name"].lower().partition(" ")

        result = TestResult(
            appName=browser,
            channel=channel or "release",
            version=sample["browser_version"],
            connection=test["data"]["connectivity"].lower(),
            url=test["data"]["testUrl"],
            platform="desktop",
            runner=os.getenv("JENKINS_URL", "unknown"),
            runId=os.getenv("BUILD_TAG", "unknown"),
            sessionState="noAuth",
            metrics=values,
        )
        print(asdict(result))

        # save the generated JSON output
        with open(f"wpt-telemetry-{test['data']['id']}.json", "w") as f:
            json.dump(asdict(result), f)

        # validate our generated JSON output against Telemetry's Pipeline schema
        # https://github.com/mozilla-services/mozilla-pipeline-schemas/blob/3ed2cc456f703501865c362512aedc4841edc084/schemas/webpagetest/webpagetest-run/webpagetest-run.1.schema.json
        with open("wpt-schema.json") as f:
            schema = json.load(f)
            validate(asdict(result), schema)

        # send to telemetry
        # first, generate a UUID
        wpt_run_uuid = uuid.uuid4().hex
        r = requests.post(
            url=f"https://incoming.telemetry.mozilla.org/submit/webpagetest/webpagetest-run/1/{wpt_run_uuid}",
            data=asdict(result),
            type="json",
        )
        r.raise_on_error()


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python send_to_telemetry.py path_to_wpt.json.sample")
        exit()
    main(*sys.argv[1:])
