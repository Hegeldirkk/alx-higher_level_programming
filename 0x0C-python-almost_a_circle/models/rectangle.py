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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Private instance attributes height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter and getter height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Private instance attributes x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter and getter x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Private instance attributes x"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter and getter y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area"""
        return (self.__height * self.__width)

    def display(self):
        """ prints in stdout"""
        for y in range(self.__y):
            print()
        for n in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """that it returns [Rectangle] (<id>)
        <x>/<y> - <width>/<height>"""
        return ("[Rectangle] (" + str(self.id) + ") " + str(self.__x) +
                "/" + str(self.__y) + " - " + str(self.__width) +
                "/" + str(self.__height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        id, width, height, x, y"""
        n = 0
        vararg = ["id", "width", "height", "x", "y"]
        if kwargs is None:
            for arg in args:
                setattr(self, vararg[n], arg)
                n += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
