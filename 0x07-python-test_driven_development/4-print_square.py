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
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError(messagError)
    for i in range(0, size):
        square = ""
        for n in range(0, size):
            square += "#"
        print(square)
    print("")
