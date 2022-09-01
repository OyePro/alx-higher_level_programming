#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    integer = 0
    roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                 "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in roman_dic.keys():
            return 0
        elif roman_dic[i] >= roman_dic[j]:
            integer += roman_dic[i]
        else:
            integer -= roman_dic[i]
    integer += roman_dic[roman_string[-1]]
    return integer
