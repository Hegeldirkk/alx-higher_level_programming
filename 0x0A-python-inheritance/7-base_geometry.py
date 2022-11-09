#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Function: BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """display reased message"""
    def area(self):
        """ area def"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value or display error"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
