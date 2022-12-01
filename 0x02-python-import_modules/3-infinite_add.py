#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv)
    sum = 0
    if num_args > 1:
        for i in range(1, num_args):
            sum += int(argv[i])
    print("{}".format(sum))
