#!/usr/bin/python3
def no_c(my_string):
    r = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            r += char
    return r
