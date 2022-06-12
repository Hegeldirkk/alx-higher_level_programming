#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        sum_magic = a + b
        return sum_magic
    operation = (a * b) - c
    return operation
