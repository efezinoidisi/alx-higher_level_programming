#!/usr/bin/python3

"""This module defines the read_file function"""


def read_file(filename=""):
    """Reads a text file and prints it to standard output.

    Args:
        filename (str): name of file to be read

    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
