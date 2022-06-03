#!/usr/bin/python3
if __name__ == "__main__":
    import sys as py
    nbarg = len(py.argv) - 1
    if nbarg == 0:
        print("0 arguments.")
    elif nbarg == 1:
        print("{} argument:\n1: {}".format(nbarg, py.argv[1]))
    elif nbarg > 1:
        print("{} arguments:".format(nbarg))
        for n in range(0, nbarg):
            print("{}: {}".format(n + 1, py.argv[n + 1]))
