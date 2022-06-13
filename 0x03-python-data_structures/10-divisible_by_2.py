#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    array = []
    for i in my_list:
        if i % 2:
            array = array + [False]
        else:
            array = array + [True]
    return array
