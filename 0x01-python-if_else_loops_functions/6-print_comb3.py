#!/usr/bin/python3
for num1 in range(0, 10, 1):
    for num2 in range(0, 10, 1):
        if num1 != num2 and num1 < num2 and (num1 != 8 or num2 != 9):
            print("{}".format(num1), end='')
            print("{}".format(num2), end=', ')
        if num1 == 8 and num2 == 9:
            print("{}{}".format(num1, num2), end="\n")
