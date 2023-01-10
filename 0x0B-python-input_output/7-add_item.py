#!/usr/bin/python3

"""This module contains a script that adds all arguments to a python
list and then saves them to a file

"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_list = argv[1:]
try:
    lst = load_from_json_file("add_item.json")
except FileNotFoundError:
    lst = []
lst.extend(arg_list)
save_to_json_file(lst, "add_item.json")
