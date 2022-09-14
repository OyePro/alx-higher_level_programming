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
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")

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

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):

        """method for getting area of square"""

        return (self.__size * self.__size)

    def my_print(self):

        """method for printing square"""

        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] + "#" * self.__size
                             for rows in range(self.__size)]))


if __name__ == "__main__":
    Square()
