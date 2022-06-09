#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ Write a function that replaces all occurrences of an element by another in a new list. """
    new_list = []
    for n in my_list:
        if n == search:
            new_list.append(replace)
        else:
            new_list.append(n)
    return new_list
