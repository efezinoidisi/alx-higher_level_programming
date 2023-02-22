#!/usr/bin/python3

# prints numbers from 0 to 99 separated by comma

for i in range(0, 100):
    if i == 99:
        print('{:02d}'.format(i))
    #else:
     #   print("{:02d},".format(i), end=" ")
