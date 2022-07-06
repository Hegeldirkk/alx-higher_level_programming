#!/usr/bin/python3
"""
Program: Alx Afrique
Auteur: Ikary Ryann
Function: add_item
"""


import json
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    input_list = load_from_json_file(filename)
except:
    input_list = []

for i in range(len(sys.argv))[1:]:
    input_list.append(sys.argv[i])
save_to_json_file(input_list, filename)
