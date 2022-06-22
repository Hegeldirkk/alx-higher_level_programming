#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """Private instance attribute: size: in class square"""
    def __init__(self, size=0):
        """main def contains Private instance attribute: size"""
        self.__size = size

    @property
    def size(self):
        """property def size(self): to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter def size(self, value): to set it: """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance method that returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print("", end="\n")
        else:
            for n in range(0, self.__size):
                for i in range(0, self.__size):
                    print("#", end="")
                print("", end="\n")
