#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header.
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    content = requests.get(url)

    if "X-Request-Id" in content.headers:
        print(content.headers.get("X-Request-Id"))
