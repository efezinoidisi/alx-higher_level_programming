#!/usr/bin/python3

# computes number a to the power of b


def pow(a, b):
    power = 1
    c = b
    if c < 0:
        c *= -1
    for i in range(c):
        power *= a

    if b < 0:
        return (1/power)
    return power
