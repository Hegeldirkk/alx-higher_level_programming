#!/usr/bin/python3
"""
Program: Alx Africa
Dev: Ikary Ryann
Desc:Write a Python script that takes in a URL,
sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    # retrieve variable
    url = argv[1]

    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))
