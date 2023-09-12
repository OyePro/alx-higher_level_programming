#!/usr/bin/python3
"""defining class is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    return a bool if obj is class of a_class or inherit from a_class
    """
    return (isinstance(obj, a_class))
