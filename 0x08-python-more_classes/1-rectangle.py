#!/usr/bin/python3

""" Creating a class Rectangle
    Module 1-rectangle
"""


class Rectangle:

    """Rectangle Class"""

    def __init__(self, width=0, height=0):

        """Initialization of class rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to retrieve width of the rectangle i.e getter
        Return:
              private instance width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set width of the rectangle i.e setter
        Return:
            new value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Method to retrieve height of the rectangle i.e getter
        Return:
              private instance height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set height of the rectangle i.e setter
        Return:
            new value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
