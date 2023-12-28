#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) < 2:
        values = {"q": ""}
    else:
        values = {"q": sys.argv[1]}
    url = "http://0.0.0.0:5000/search_user"

    content = requests.post(url, data=values)

    try:
        content_json = content.json()

        if content_json:
            Id = content_json.get("id")
            name = content_json.get("name")
            print("[{}] {}".format(Id, name))
        else:
            print("No result"

    except ValueError:
        print("Not a valid JSON")
