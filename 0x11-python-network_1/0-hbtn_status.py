#!/usr/bin/python3
"""
Program: Alx Africa
Dev: Ikary Ryann
Desc:Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        res = resp.read()
    print('Body Response:')
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
    print("\t- utf8 content: {}".format(res.decode('utf-8')))
