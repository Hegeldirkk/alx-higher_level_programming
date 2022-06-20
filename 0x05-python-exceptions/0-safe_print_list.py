#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb = 0
    for n in range(0, x):
        try:
            print("{:d}".format(my_list[n]), end='')
            nb = x
        except IndexError:
            nb = x - 2
            break
    print("")
    return nb
