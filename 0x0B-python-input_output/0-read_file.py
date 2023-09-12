#!/usr/bin/python3
"""Defining function read_file"""


def read_file(filename=""):
    """method to read a textfile and print to standard output"""
    with open(filename, encoding="utf-8") as f:
        read_name = f.read()
    print(read_name, end="")
