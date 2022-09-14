#!/usr/bin/python3

"""Defining a class Square
   Module 6-square
"""


class Square:

    """Square class"""

    def __init__(self, size=0, position=(0, 0)):

        """Initialize square class"""

        self.__size = size
        self.__position = position
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")

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
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):

        """getter for position"""

        return self.__position

    @position.setter
    def position(self, value):

        """setter for position"""

        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):

        """method for getting area of square"""

        return (self.__size * self.__size)

    def my_print(self):

        """method for printing square"""

        if self.__size == 0:
            print("")
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
