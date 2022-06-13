#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    size = 0
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    for n in my_list:
        weight += (n[0] * n[1])
        size += n[1]
    return (weight / size)
