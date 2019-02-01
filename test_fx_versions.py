#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json


def get_webpagetest_fx_version_json(wpt_json):
    with open("wpt.json") as f:
        data = json.load(f)

    for test in data:

        webpagetest_fx_version_json = test["data"]["median"]["firstView"]["browser_version"]
        fx_version = webpagetest_fx_version_json

        print(fx_version)

fx_product_details_json_url = ("https://product-details.mozilla.org/1.0/firefox_versions.json")

        # def get_webpagetest_fx_version():


        # def compare_fx_versions(fx_product_details_json, webpagetest_fx_version_json):
