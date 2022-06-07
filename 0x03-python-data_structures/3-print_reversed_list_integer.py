#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for n in range(len(my_list)+1):
        if n != 0:
            print("{}".format(my_list[-n]))
