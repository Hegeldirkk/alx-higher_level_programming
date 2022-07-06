#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Function: inherits_from
"""


def inherits_from(obj, a_class):
    """eturns True if the object is exactly
     of a class that inherited (directly or indirectly) 
     otherwise False.
    args: obj (variable)
    a_class (type test)
    """
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    return False
