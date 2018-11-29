import json
# from pprint import pprint
import os
import sys

from datadog import api, initialize, statsd


options = {
    "api_key": os.getenv("DATADOG_API_KEY"),
    "app_key": os.getenv("DATADOG_APP_KEY"),
    "statsd_host": "localhost",
    "statsd_port": "8125",
}


def main(path):

    initialize(**options)

    dbl_name = "WebPageTest"
    dbls = api.DashboardList.get_all()["dashboard_lists"]
    # pprint(dbls)
    try:
        dbl = next(dbl for dbl in dbls if dbl["name"] == dbl_name)
        print(f"Using existing {dbl_name} dashboard list")
    except StopIteration:
        print(f"Creating {dbl_name} dashboard list")
        dbl = api.DashboardList.create(name=dbl_name)

    tbdata = {}
    tbs = api.Timeboard.get_all()["dashes"]
    # pprint(tbs)

    with open(path) as f:
        data = json.load(f)

    with open("metrics.json") as f:
        metrics = json.load(f)

    for test in data:
        target_url = test["data"]["testUrl"]

        tb = tbdata.setdefault(target_url, {})
        tb["title"] = target_url
        tb["description"] = f"WebPageTest results for {target_url}"
        graphs = tb.setdefault("graphs", [])

        sample = test["data"]["median"]["firstView"]
        browser_name = sample["browser_name"]
        browser_version = sample["browser_version"]
        label = test["data"]["label"].replace('-', '_')
        print(f"{target_url} - {browser_name} ({browser_version})")
        requests = []
        for metric in metrics:
            name = metric['name']
            title = f"{metric['description']} ({metric['unit']})"
            query = f"avg:wpt.batch.{label}.median.firstView.{name}{{*}}"
            try:
                graph = next(g for g in graphs if g["title"] == title)
                requests = graph["definition"]["requests"]
                if query not in requests:
                    requests.append({"q": query})
            except StopIteration:
                graphs.append({
                    "title": title,
                    "definition": {
                        "requests": [{"q": query}],
                        "viz": "timeseries",
                    }
                })
            value = test["data"]["median"]["firstView"][name]
            print(f"- {name}: {value}")
            statsd.gauge(f"wpt.batch.{label}.median.firstView.{name}", value)

    # pprint(tb)            
    for item in tbdata.values():
        title = item["title"]
        description = item["description"]
        graphs = item["graphs"]

        try:
            tb = next(tb for tb in tbs if tb["title"] == title)
            print(f"Updating {title} timeboard")
            tb = api.Timeboard.update(
                tb["id"],
                title=title,
                description=description,
                graphs=graphs,
            )
        except StopIteration:
            print(f"Creating {title} timeboard")
            tb = api.Timeboard.create(
                title=title,
                description=description,
                graphs=graphs,
            )

        # pprint(tb)
        print(f"Adding {title} timeboard to {dbl_name} dashboard list")
        api.DashboardList.add_items(dbl["id"], dashboards=[{
            "type": "custom_timeboard",
            "id": tb["dash"]["id"]}])


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python send_to_datadog.py path")
        exit()
    main(*sys.argv[1:])
