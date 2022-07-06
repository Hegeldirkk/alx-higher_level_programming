#!/usr/bin/python3
"""
Auteur: IKary Ryann
Function: inherits
Class: MyList
Method: def print_sorted(self)
"""


class MyList(list):
    """ Public instance method """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        print(sorted(self))
