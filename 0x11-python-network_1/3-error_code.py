#!/usr/bin/python3
"""
Program: Alx Africa
Dev: Ikary Ryann
Desc:Write a Python script that takes in a URL,
sends a request to the URL and displays the
body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv

    # retreive variable
    url = argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            res = resp.read()
            print("{}".format(res.decode('utf-8')))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
