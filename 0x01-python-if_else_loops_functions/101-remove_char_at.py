#!/usr/bin/python3


def remove_char_at(str, n):
    new_str = ""
    for values in enumerate(str):
        if values[0] != n:
            new_str += values[1]

    return new_str
