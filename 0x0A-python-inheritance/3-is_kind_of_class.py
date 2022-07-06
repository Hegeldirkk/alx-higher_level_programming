#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Function: is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance
    otherwise False
    args: obj (variable)
    a_class (type test)
    """
    if issubclass(type(obj), a_class):
        return True
    return False
