#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""


if __name__ == "__main__":

    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode("utf-8")
            print(content)
    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")
