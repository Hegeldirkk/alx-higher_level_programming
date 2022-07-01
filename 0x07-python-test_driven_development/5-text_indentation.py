#!/usr/bin/python3
""" Text Indentattion """


def text_indentation(text):
    """ prints a text with 2 new lines after
    each of these characters: ., ? and :
    arg: text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    characters = [".", "?", ":"]
    for n in text:
        print("{}".format(n), end='')
        if n in characters:
            print("", end='\n\n')
