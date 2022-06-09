#!/usr/bin/python3
def uniq_add(my_list=[]):
    adds_list = []
    adds = 0
    for n in my_list:
        if n in adds_list:
            adds += 0
        else:
            adds_list.append(n)
            adds += n
    return adds
