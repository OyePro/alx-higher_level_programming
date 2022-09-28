#!/usr/bin/python3
"""defining function add_integer to add a+b"""


def add_integer(a, b=98):
    """
    Return: a + b as int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
