#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        resultf = fct(*args)
        return resultf
    except (IndexError, ZeroDivisionError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
