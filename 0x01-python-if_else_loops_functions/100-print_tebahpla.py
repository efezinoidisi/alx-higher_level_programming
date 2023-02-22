#!/usr/bin/python3

alpha = ""
for i in range(122, 96, -1):
    if i % 2 != 0:
        alpha += chr(i - 32)
    else:
        alpha += chr(i)
print("{}".format(alpha))
