#!/usr/bin/python3

"""This module defines the append_write function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file

    Args:
        filename (str): name of file to be written to
        text (str): string to be added

    Return:
         number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        num = f.write(text)
        return num
