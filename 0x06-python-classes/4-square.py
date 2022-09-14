#!/usr/bin/python3

"""Defining a Class Square
   Module 4-square
"""


class Square:

    """Square Class"""

    def __init__(self, size=0):

        """Initializing Square class"""

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):

        """getter for size of the square"""

        return self.__size

    @size.setter
    def size(self, value):

        """setter for size of the square"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """method for finding area of the square"""

        return self.__size * self.__size
