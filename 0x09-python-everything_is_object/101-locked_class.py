#!/usr/bin/python3
"""Write a class LockedClass with no class"""


class LockedClass:
    """
    prevents the user from dynamically 
    creating new instance attributes
    """
    __slots__ = ["first_name"]
