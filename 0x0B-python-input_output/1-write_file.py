#!/usr/bin/python3
"""Defining function write_file"""


def write_file(filename="", text=""):
    """
    this function write string store in text to filename
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return (f.write(text))
