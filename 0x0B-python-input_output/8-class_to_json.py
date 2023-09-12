#!/usr/bin/python3
"""Defining function class_to_json"""


def class_to_json(obj):
    """
    returns dictionary descriptions with simple data structure
    """
    return (obj.__dict__)
