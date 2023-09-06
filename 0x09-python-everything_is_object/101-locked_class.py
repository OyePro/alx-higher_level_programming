#!/usr/bin/python3

"""Defining LockedClass with no class or object attribute,
that prevents the user from
dynamically creating new instance attributes
"""


class LockedClass:
    """Class LockedClass which prevent dynamically
    creating new instance attributes except 'first_name'.
    """
    __slots__ = ['first_name']
