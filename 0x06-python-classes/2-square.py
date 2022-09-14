#!/usr/bin/python3i

"""Defining class Square
   Module 2-square
"""


class Square:

    """Square Class"""

    def __init__(self, size=0):

        """Initialize Square class"""

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
