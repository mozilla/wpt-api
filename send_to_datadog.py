import json
import sys

from datadog import initialize, statsd


options = {
    "statsd_host": "localhost",
    "statsd_port": "8125",
}

# these metrics are roughly in order of occurrence & metadata
metrics = [
    "TTFB",
    "render",
    "firstPaint",
    "timeToDOMContentFlushed",
    "SpeedIndex",
    "bytesInDoc",
    "visualComplete",
    "requestsFull",
    "browser_version"
]


def main(path):

    with open(path) as f:
        data = json.load(f)

    initialize(**options)

    for test in data:
        label = test["data"]["label"]
        print(f"{label}")
        for metric in metrics:
            value = test["data"]["median"]["firstView"][metric]
            print(f"- {metric}: {value}")
            statsd.gauge(f"wpt.batch.{label}.median.firstView.{metric}", value)


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python send_to_datadog.py path")
        exit()
    main(*sys.argv[1:])
