#!/usr/bin/python3

"""This module defines the write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file

    Args:
        filename (str): name of file to be read

    Return:
         number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        num = f.write(text)
        return num
