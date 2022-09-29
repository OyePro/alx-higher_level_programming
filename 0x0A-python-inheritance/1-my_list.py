#!/usr/bin/python3
"""Defining class Mylist which inherit class list"""


class MyList(list):
    """
    class Mylist
    """

    def print_sorted(self):
        """
        method print_sorted which return sorted list in ascending order
        """
        print(sorted(self))
