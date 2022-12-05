#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds two tuples

    Args:
    tuple_a: first tuple
    tuple_b: second tuple

    Returns:
    a tuple with 2 integers

    """
    first = tuple_a + (0, 0)
    second = tuple_b + (0, 0)
    temp = (first[0] + second[0], first[1] + second[1],)

    return tuple(temp)
