#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        new_tuple = (length, sentence[0],)
    else:
        new_tuple = (length, "None",)
    return new_tuple
