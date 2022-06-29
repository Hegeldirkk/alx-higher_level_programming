#!/usr/bin/python3
"""
function that adds 2 integers.
it check if is an integers or floats
"""


def add_integer(a, b=98):
    """inside my addition function
    two args:
    a - must be integers or floats
    b - must be integers or floats
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
