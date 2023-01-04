#!/usr/bin/python3
"""
 This is the 5-text_indentation module.

 This module supplies one function, text_indentation(). ~

"""


def text_indentation(text):
    """This function prints a text with 2 new lines
    after these characters : ? .

    Args:
        text (str): the given text

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    check = False
    for letter in text:
        if letter != " ":
            check = True
        if letter in ":.?":
            print(f"{letter}")
            print()
            check = False
        elif check:
            print(f"{letter}", end="")
