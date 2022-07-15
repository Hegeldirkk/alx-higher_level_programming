#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Project: 0x0C. Python - Almost a circle
Class: Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """Private instance attributes
    each with its own public getter and setter"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Private instance attributes width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter and getter width"""
        if type(value) is not int:
            raise Exception("width attributes must be an integer")
        elif value <= 0:
            raise ValueError("width attributes must > 0")
        self.__width = value

    @property
    def height(self):
        """Private instance attributes height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter and getter height"""
        if type(value) is not int:
            raise Exception("height attributes must be an integer")
        elif value <= 0:
            raise ValueError("height attributes must > 0")
        self.__height = value

    @property
    def x(self):
        """Private instance attributes x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter and getter x"""
        if type(value) is not int:
            raise Exception("x attributes must be an integer")
        elif value < 0:
            raise ValueError("x attributes must > 0")
        self.__x = value

    @property
    def y(self):
        """Private instance attributes x"""
        return self.__y

    @x.setter
    def y(self, value):
        """setter and getter y"""
        if type(value) is not int:
            raise Exception("y attributes must be an integer")
        elif value < 0:
            raise ValueError("y attributes must > 0")
        self.__y = value
