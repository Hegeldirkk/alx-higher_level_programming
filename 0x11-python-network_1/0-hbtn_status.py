#!/usr/bin/python3
"""
Program: Alx Africa
Dev: Ikary Ryann
Desc:Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        res = response.read()
        print('Body Response:')
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode('utf-8')))
