#!/usr/bin/python3
"""
Program: Alx Africa
Dev: Ikary Ryann
Desc:Write a Python script that
fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests

    res = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(res.content.decode('utf-8')))
