#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST request to the
passed URL wit the email as a parameter, and displays the body of the response
"""


if __name__ == "__main__":

    import sys
    import requests

    url = sys.argv[1]
    values = {"email": sys.argv[2]}

    content = requests.post(url, data=values)
    print(content.text)
