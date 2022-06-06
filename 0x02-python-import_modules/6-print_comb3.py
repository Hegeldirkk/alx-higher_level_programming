#!/usr/bin/python3
a = 1
for n in range(0, 9):
    for i in range(a, 10):
        if i != n :
            print("{:1d}".format(n), end="")
            if n != 8 :
                print("{:1d}".format(i), end=", ")
            else:
                print("{:1d}".format(i), end="\n")
    a = a + 1
