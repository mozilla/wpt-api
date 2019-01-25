from dataclasses import asdict, dataclass
import json
import sys


@dataclass
class TestResult:
    appName: str
    channel: str
    version: str
    url: str
    metrics: dict


def main(path):
    with open(path) as f:
        data = json.load(f)

    for test in data:
        sample = test["data"]["median"]["firstView"]
        metrics = {"TTFB": TTFB, "startRender": startRender, "firstPaint": firstPaint,
                    "timeToContentfulPaint": timeToContentfulPaint,
                    "domContentFlushed":, "timeToFirstInteractive", "pageLoadTime": pageLoadTime,
                    "SpeedIndex": SpeedIndex, "bytesInDoc": bytesInDoc, "visualComplete": visualComplete, "requestsFull": requestsFull}
        result = TestResult(
            appName=sample["browser_name"],
            channel="",
            version=sample["browser_version"],
            url=test["data"]["testUrl"],
            metrics=metrics)
        print(result)
        print(metrics)
        print(asdict(result))
        print(json.dumps(asdict(result)))
        # send to telemetry


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python send_to_telemetry.py path")
        exit()
    main(*sys.argv[1:])
