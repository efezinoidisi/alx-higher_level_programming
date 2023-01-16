#!/usr/bin/python3
"""
The base module contains the class Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method returns the JSON string representation of
         list_dictionaries

        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
