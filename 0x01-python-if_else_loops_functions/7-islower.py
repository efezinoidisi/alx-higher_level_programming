#!/usr/bin/python3

# checks for lowerxase character

def islower(c):
    num = ord(c)
    if num >= 97 and num <= 122:
        return True
    else:
        return False
