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
        """Prints the list, in ascending sort."""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
