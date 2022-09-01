#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        dict = {}
        tmp = {}
        for key, value in a_dictionary.items():
            new_value = value * 2
            tmp = {key: new_value}
            dict.update(tmp)
        return (dict)
    return None
