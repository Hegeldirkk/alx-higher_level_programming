#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Function: read_file
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
