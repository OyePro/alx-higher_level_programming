#!/usr/bin/python3
"""Defining function append_write"""


def append_write(filename="", text=""):
    """
    append a string to a file
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return (f.write(text))
