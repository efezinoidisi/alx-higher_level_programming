#!/usr/bin/python3


def safe_function(fct, *args):
    from sys import stderr
    try:
        fct(args[0], args[1])
    except Exception as err:
        print("Exception: {}".format(err), file =stderr)
