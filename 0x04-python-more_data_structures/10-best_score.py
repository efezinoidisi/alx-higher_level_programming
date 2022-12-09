#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        maxi = 0
        for i, j in a_dictionary.items():
            if j > maxi:
                maxi = j
                item = i
        return a_dictionary[item]
    return
