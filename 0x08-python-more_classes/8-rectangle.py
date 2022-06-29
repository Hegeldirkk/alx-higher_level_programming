#!/usr/bin/python3
"""Write a class Rectangle (based on 3-rectangle.py)"""


class Rectangle:
    """Retreive width and heigth in Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initstate function rectangle"""
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    def area(self):
        """calcul area of retangle"""
        area = (self.__height * self.__width)
        return area

    def perimeter(self):
        """calcul perimeter of retangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        """should print the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""

        rect = []
        for n in range(self.__height):
            for i in range(self.__width):
                rect.append(str(self.print_symbol))
            if n != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """should return a string representation of the rectangle"""
        represent = "Rectangle(" + str(self.__width)
        represent += ", " + str(self.__height) + ")"
        return represent

    def __del__(self):
        """Print the message Bye rectangle (being 3 dots not ellipsis)"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        biggest rectangle based on the area
        args:
        rect_1 = instance of Rectangle
        rect_2 = instance of Rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
