#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        print('')
    else:
        for n in reversed(range(len(my_list))):
            print("{}".format(my_list[n]))
