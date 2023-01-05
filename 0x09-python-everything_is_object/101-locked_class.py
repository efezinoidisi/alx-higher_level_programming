#!/usr/bin/python3
""" This module contains the LockedClass class"""


class LockedClass:
    """A class that prevents the user from dynamically creating new instance
    attributes except if it is called `first_name`

    """
    __slots__ = ['first_name']
