#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Function: is_same_class
"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly
    otherwise False.
    args: obj (variable)
    a_class (type test)
    """
    if type(obj) is a_class:
        return True
    return False
