#!/usr/bin/python3

# prints numbers from 1 to 100


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz ", end="")
        elif i % 3 == 0:
            print(f"Fizz ", end="")
        elif i % 5 == 0:
            print(f"Buzz ", end="")
        else:
            print(f"{i:d} ", end="")
