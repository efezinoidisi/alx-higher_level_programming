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

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the list of the JSON string representation

        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string representation of list_objs
        to a file
        """
        if not list_objs:
            list_objs = []
        with open(f"{cls.__name__}.json", 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_objs), f)
