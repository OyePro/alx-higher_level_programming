#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last = (int(repr(-number)[-1]))
    else:
        last = int(repr(number)[-1])
    print(f"{last}", end="")
    return (last)
