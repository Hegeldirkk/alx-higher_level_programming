#!/usr/bin/python3
"""
Program: Alx Africa
Dev: Ikary Ryann
Desc:Write a Python script that takes in a URL
and an email, sends a POST request to the passed
URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv

    # retrieve variable
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        res = resp.read()
        print("{}".format(res.decode('utf-8')))
