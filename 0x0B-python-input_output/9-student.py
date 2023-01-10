#!/usr/bin/python3
"""
This module defines the Student class

"""


class Student():
    """

    A class that defines a student

    Attributes:
          first_name (str): first name of student
          last_name (str): last name of student
          age (int): student's age

    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of an instance of Student"""
        return vars(self)
