#!/usr/bin/python3
"""defining function is_same_class"""


def is_same_class(obj, a_class):
    """
    returns a bool, if obj is an instance of a_class
    """
    return (type(obj) is a_class)
