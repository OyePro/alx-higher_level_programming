#!/usr/bin/python3

"""Defining class Square
   Module 101-Square
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

        """Method for getting area of the square"""

        return (self.__size * self.__size)

    def my_print(self):

        """Method for printing the square"""

        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] + "#" * self.__size
                             for rows in range(self.__size)]))

    def __str__(self):

        """printing the square by calling Square()"""

        square = ""
        if self.__size == 0:
            return square

        square += "\n" * self.__position[1]
        square += "\n".join([" " * self.__position[0] + "#" * self.__size
                             for rows in range(self.__size)])
        return square
