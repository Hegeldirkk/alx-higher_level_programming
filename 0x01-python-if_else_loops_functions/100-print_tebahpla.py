#!/usr/bin/python3
c = 0
for n in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(n - c)), end="")
    c = 32 if c == 0 else 0
