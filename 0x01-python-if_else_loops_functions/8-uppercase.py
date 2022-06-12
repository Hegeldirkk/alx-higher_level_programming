#!/usr/bin/python3
def uppercase(c):
    r = ''
    for i in c:
        a = ord(i)
        if a >= 97 and a <= 122:
            a = a - 32
            r += chr(a)
        else:
            r += i
    print("{:s}".format(r))
