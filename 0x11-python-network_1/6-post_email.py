#!/usr/bin/python3
"""
Program: ALx Africa
Dev: Ikary Ryann
Desc:Write a Python script that takes in a URL
and an email address, sends a POST request to the
passed URL with the email as a parameter, and
finally displays the body of the response.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    # retreive variable
    url = argv[1]
    values = {'email': argv[2]}

    res = requests.post(url, data=values)
    print('{}'.format(res.text))
