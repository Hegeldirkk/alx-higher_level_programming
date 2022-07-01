#!/usr/bin/python3
""" Text Indentattion """


def text_indentation(text):
    """ prints a text with 2 new lines after
    each of these characters: ., ? and :
    arg: text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    count = 0
    toget = ""
    characters = [".", "?", ":"]
    for n in range(len(text)):
        if text[n] in characters:
            toget += text[n] + '\n\n'
        else:
            if (n != 0 and
                (text[n - 1] in characters or text[n - 1] is ' ') and
               text[n] is ' '):
                pass
            else:
                toget += text[n]
    print(toget, end="")
