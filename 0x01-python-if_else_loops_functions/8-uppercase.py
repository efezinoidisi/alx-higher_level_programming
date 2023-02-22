#!/usr/bin/python3

def uppercase(str):
    str_upper = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            str_upper += chr(ord(char) - 32)
        else:
            str_upper += char

    print(str_upper)
