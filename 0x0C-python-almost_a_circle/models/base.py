#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Project: 0x0C. Python - Almost a circle
Class: first class Base
"""


class Base:
    """The goal of it is to manage id
    attribute in all your future classes
    and to avoid duplicating the same code
    (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
