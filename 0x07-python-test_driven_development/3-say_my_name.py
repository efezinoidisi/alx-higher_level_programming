#!/usr/bin/python3
"""
 This is the 3-say_my_name module.

 This module supplies one function, say_my_name(). for example,

 >>> say_my_name("John Smith")
 My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """This function prints:
      My name is [first_name] [last_name]

    Args:
        first_name (str): given first name
        last_name (str): given surname

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
