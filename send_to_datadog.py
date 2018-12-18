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
    "timeToContentfulPaint",
    "timeToDOMContentFlushed",
    "timeToFirstInteractive",
    "SpeedIndex",
    "bytesInDoc",
    "visualComplete",
    "requestsFull",
    "browser_name",
    "browser_version"
]


def main(path):

    with open(path) as f:
        data = json.load(f)

    initialize(**options)

    for test in data:
        sample = test["data"]["median"]["firstView"]
        tags = [
            "url:" + test["data"]["testUrl"],
            "browser_name:" + sample["browser_name"],
            "browser_version:" + sample["browser_version"]]
        label = test["data"]["label"]
        print(f"{label}")
        for metric in metrics:
            value = sample[metric]
            print(f"- {metric}: {value}")
            statsd.gauge(f"wpt.median.firstView.{metric}", value, tags=tags)


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python send_to_datadog.py path")
        exit()
    main(*sys.argv[1:])
