#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Function: write_file
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters
    args: filename, text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
