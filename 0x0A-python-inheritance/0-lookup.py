#!/usr/bin/python3
"""Defining a function lookup"""


def lookup(obj):
    """
    Return the list of attributes and methods in ibj
    """
    return (list(dir(obj)))
