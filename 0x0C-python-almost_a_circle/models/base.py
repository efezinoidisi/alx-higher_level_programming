#!/usr/bin/python3
"""
The base module contains the class Base
"""


class Base:
    """This is the base class for all other classes in this project.

    Attributes:
        nb_objects (int): number of objects

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method for the Base class.

        Args:
        id (int): id of each instance

        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
