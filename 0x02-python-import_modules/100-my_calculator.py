#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    num_args = len(argv) - 1
    operators = ['+', '-', '*', '/']

    if num_args != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    operator = argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
