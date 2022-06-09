#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_adict = {}
    for k, v in a_dictionary.items():
        new_adict.update({k: (v * 2)})
    return new_adict
