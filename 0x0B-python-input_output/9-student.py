#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Function: Student
"""


class Student:
    """ Class Student"""

    def __init__(self, first_name, last_name, age):
        """args: first_name, last_name, age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary"""
        return self.__dict__