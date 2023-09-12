#!/usr/bin/python3
"""defining class MyInt"""


class MyInt(int):
    """
    class MyInt inherits int
    """

    def __init__(self, ints):
        """
        initialization of the class
        """
        self.ints = ints

    def __eq__(self, value):
        """
        return false if it is equal
        """
        return (self.ints != value)

    def __ne__(self, value):
        """
        return True if it is equal
        """
        return (self.ints == value)
