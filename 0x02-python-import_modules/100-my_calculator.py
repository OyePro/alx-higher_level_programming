#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    calc = argv
    length = len(calc) - 1
    if length < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(calc[1])
    b = int(calc[3])
    sign = (calc[2])
    if sign == '+':
        print("{} {} {} = {}".format(a, sign, b, add(a, b)))
    elif sign == '-':
        print("{} {} {} = {}".format(a, sign, b, sub(a, b)))
    elif sign == "*":
        print("{} {} {} = {}".format(a, sign, b, mul(a, b)))
    elif sign == '/':
        print("{} {} {} = {}".format(a, sign, b, div(a, b)))
    else:  # sign != '+' or sign != '-' or sign != '*' or sign != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
