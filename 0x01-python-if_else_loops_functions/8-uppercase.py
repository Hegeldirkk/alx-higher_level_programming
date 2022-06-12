#!/usr/bin/python3
def uppercase(c):
    for i in c:
        a = ord(i)
        if a >= 97 and a <= 122:
            a = a - 32
        print("{}".format(chr(a), end=''))
    print()
