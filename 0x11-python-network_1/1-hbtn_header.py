#!/usr/bin/python3
"""
Program: ALx Africa
Dev: Ikary Ryann
Desc: Write a Python script that takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as resp:
        res = resp.info()
        print(res['X-Request-Id'])
