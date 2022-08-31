#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = 0
    mult = []
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            mult.append(True)
        else:
            mult.append(False)
        i += 1
    return (mult)
