#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""


if __name__ == "__main__":

    import sys
    import requests

    url = sys.argv[1]

    try:
        content = requests.get(url)
        content.raise_for_status()
        print(content.text)
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and hasattr(e.response, 'status_code'):
            print(f"Error code: {e.response.status_code}")
