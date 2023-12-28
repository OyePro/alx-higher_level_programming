#!/usr/bin/python3
# A Python script that fetches https://alx-intranet.hbtn.io/status


if __name__ == "__main__":

    import requests
    url = "https://alx-intranet.hbtn.io/status"

    content = requests.get(url)

    print("Body response:")
    print("\t- type:", type(content.text))
    print("\t- content:", content.text)
