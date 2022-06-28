#!/usr/bin/python3
"""Write a class Rectangle (based on 1-rectangle.py)"""


class Rectangle:
    """Retreive width and heigth in Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initstate function rectangle"""
        self.__height = height
        self.__width = width

    def area(self):
        """calcul area of retangle"""
        area = (self.__height * self.__width)
        return area

    @property
    def width(self):
        """property width retreive it"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter width set it"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property height retreive it"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter height set it"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """calcul perimeter of retangle"""
        if self.__height == 0 and self.__width == 0:
            return 0
        else:
            return ((self.__height + self.__width) * 2)
