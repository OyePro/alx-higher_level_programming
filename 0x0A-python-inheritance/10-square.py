#!/usr/bin/python3
"""defining class Square which inherits class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size):
        """
        Initialization of class Square
        Arg:
            size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """methods for printing area of square"""
        return ((self.__size)**2)

    def __str__(self):
        """printing square are [Rectangle] <size>/size>"""
        return ("[Rectangle] {:d}/{:d}".format(self.__size, self.__size))
