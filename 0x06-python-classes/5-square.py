#!/usr/bin/python3

"""Defining a Square Class
   Module 5-square
"""


class Square:

    """Square class"""

    def __init__(self, size=0):

        """Initialize square class"""

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):

        """getter for size"""

        return self.__size

    @size.setter
    def size(self, value):

        """setter for size"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """method for getting area of Square"""

        return self.__size * self.__size

    def my_print(self):

        """method for printing square"""

        if self.__size == 0:
            print()
        else:
            print("\n".join(["#" * self.__size for rows in
                  range(self.__size)]))
