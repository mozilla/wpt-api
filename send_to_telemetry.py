from dataclasses import asdict, dataclass
from jsonschema import validate
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

    # we need to validate to https://github.com/mozilla-services/mozilla-pipeline-schemas/blob/3ed2cc456f703501865c362512aedc4841edc084/schemas/webpagetest/webpagetest-run/webpagetest-run.1.schema.json

    for test in data:
        build_tag = str(os.getenv("BUILD_TAG", "unknown"))
        print("BUILD_TAG is: ", build_tag)

        jenkins_URL = str(os.getenv("JENKINS_URL", "unknown"))
        print("JENKINS_URL is: ", jenkins_URL)

    for test in data:
        sample = test["data"]["median"]["firstView"]
        # print(sample)

        for measure in metrics:
            name = measure["name"]
            medianMetric = test["data"]["median"]["firstView"]
            print("Metric name: ", name)
            print("Median metric: ", medianMetric)
            values = {name: {"firstView": medianMetric}}

            # values[sample][name]["firstView"] = {}
            # print(values)
            # values["firstView"][metric] = {}
            # print("Values dict: ", values)
            for metric in metrics:
                try:
                    value = test["data"]["median"]["firstView"][name]
                    print("Metric value: ", value)
                    # values = {"firstView": {}}
                    if value is not None:
                        values[name]["firstView"] = value
                        print(values)
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
        # print(json.dumps(asdict(result)))
        # with open(f"wpt-telemetry-{test['data']['id']}.json", "w") as f:
        #   json.dump(asdict(result), f)

        # send to telemetry
        # r = requests.post(url="", data=asdict(result), type="json")
        # r.raise_on_error()
schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "additionalProperties": false,
  "description": "Web-performance metrics",
  "properties": {
    "appName": {
      "type": "string"
    },
    "channel": {
      "type": "string"
    },
    "connection": {
      "type": "string"
    },
    "metrics": {
      "additionalProperties": {
        "properties": {
          "firstView": {
            "anyOf": [
              {
                "required": [
                  "median"
                ]
              },
              {
                "required": [
                  "standardDeviation"
                ]
              }
            ],
            "properties": {
              "median": {
                "type": "number"
              },
              "standardDeviation": {
                "type": "number"
              }
            },
            "type": "object"
          }
        },
        "required": [
          "firstView"
        ],
        "type": "object"
      },
      "type": "object"
    },
    "platform": {
      "enum": [
        "desktop",
        "mobile"
      ],
      "type": "string"
    },
    "runId": {
      "type": "string"
    },
    "runner": {
      "type": "string"
    },
    "sessionState": {
      "enum": [
        "auth",
        "noAuth"
      ],
      "type": "string"
    },
    "url": {
      "type": "string"
    },
    "version": {
      "type": "string"
    }
  },
  "required": [
    "appName",
    "channel",
    "version",
    "connection",
    "url",
    "platform",
    "runner",
    "runId",
    "sessionState",
    "metrics"
  ],
  "title": "webpagetest-run",
  "type": "object"
}

validate(instance=TestResult, schema=schema)

if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python send_to_telemetry.py path")
        exit()
    main(*sys.argv[1:])
