#!/usr/bin/python3
"""
Say my name
function that print my name
"""


def say_my_name(first_name, last_name=""):
    """
    Print sentenses with 
    the first and last name

    Args: 
        first_name
        last_name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name), end="\n")
