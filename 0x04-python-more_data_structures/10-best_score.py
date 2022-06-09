#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = 0
        best_key = ""
        for n in list(a_dictionary.keys()):
            if a_dictionary[n] > best_score:
                best_score = a_dictionary[n]
                best_key = n
        return best_key
    else:
        return None
