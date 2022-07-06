#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Function: Student ased on 9-student.py
"""


class Student:
    """ Class Student"""

    def __init__(self, first_name, last_name, age):
        """args: first_name, last_name, age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary"""
        if attrs is not None:
            return {key: value for key,
                    value in self.__dict__.items() if key in attrs}
        else:
            return self.__dict__
