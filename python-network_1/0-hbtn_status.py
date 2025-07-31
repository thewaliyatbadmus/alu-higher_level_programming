#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
