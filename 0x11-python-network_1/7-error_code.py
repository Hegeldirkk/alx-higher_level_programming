#!/usr/bin/python3
"""
Program: ALx Africa
Dev: Ikary Ryann
Desc:Write a Python script that takes in a URL,
sends a request to the URL and displays the body
of the response.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    # retrieve variable
    url = argv[1]

    try:
        res = requests.get(url)
        res.raise_for_status()
        print('{}'.format(res.text))
    except requests.exception.RequestException as e:
        print("Error code: {}".format(e.response.status_code))
