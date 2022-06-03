#!/usr/bin/python3
if __name__ == "__main__":
    import sys as py
    nbarg = len(py.argv) - 1
    sum = 0
    if nbarg == 0:
        print("0")
    elif nbarg > 0:
        for n in range(0, nbarg):
            sum = sum + int(py.argv[n + 1])
        print("{:d}".format(sum))
