#!/usr/bin/python3
""" Square function with charater #"""


def print_square(size):
    """
    arg: size is the length
    it must be an integer
    """
    messagError = "size must be an integer"
    if type(size) is not int:
        raise TypeError(messagError)
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(0, size):
        square = ""
        for n in range(0, size):
            square += "#"
        print(square)
