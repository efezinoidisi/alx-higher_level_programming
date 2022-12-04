#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        max_int = my_list[0]
        for i in my_list:
            if i > max_int:
                max_int = i
    else:
        max_int = "None"
    return max_int
