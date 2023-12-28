#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST request to the
passed URL wit the email as a parameter, and displays the body of the response
"""


if __name__ == "__main__":

    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values).encode("utf-8")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        content = response.read().decode("utf-8")
    print(content)
