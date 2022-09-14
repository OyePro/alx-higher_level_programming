#!/usr/bin/python3

"""Define a class Square
   Module 102-square
"""


class Square:

    """Square Class"""

    def __init__(self, size=0):

        """Initialize a new class"""

        self.__size = size

    @property
    def size(self):

        """Getter for size of the square"""

        return self.__size

    @size.setter
    def size(self, value):

        """Setter for size of the square"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """Area of the square"""

        return (self.__size * self.__size)

    def __eq__(self, other):

        """ == Comparator """

        return self.area() == other.area()

    def __ne__(self, other):

        """ != Comparator """

        return self.area() != other.area()

    def __gt__(self, other):

        """ > Comparator """

        return self.area() > other.area()

    def __ge__(self, other):

        """ >= Comparator """

        return self.area() >= other.area()

    def __lt__(self, other):

        """ < Comparator """

        return self.area() < other.area()

    def __le__(self, other):

        """ <= Comparator """

        return self.area() <= other.area()


if __name__ == "__main__":
    Square()
