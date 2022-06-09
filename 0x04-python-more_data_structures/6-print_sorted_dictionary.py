#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())
    values = a_dictionary.values()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
