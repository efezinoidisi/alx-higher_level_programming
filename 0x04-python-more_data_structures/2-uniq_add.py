#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique = set(my_list)
    new_list = list(unique)
    return sum(new_list)
