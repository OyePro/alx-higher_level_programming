#!/usr/bin/python3
"""
function that adds a new attribute to an object if it is possible
"""


def add_attribute(obj, attribute, value):
    """
    Adding attribute or raising Exception
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
