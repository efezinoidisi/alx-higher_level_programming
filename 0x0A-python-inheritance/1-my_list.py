#!/usr/bin/python3
""" This module defines the MyList class """


class MyList(list):
    """
    This class inherits from the list class

    """
    def print_sorted(self):
        """prints a sorted list """
        print(sorted(self))
