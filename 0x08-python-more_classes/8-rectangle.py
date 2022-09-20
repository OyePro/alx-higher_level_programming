#!/usr/bin/python3

""" Creating a class Rectangle
    Module 3-rectangle
"""


class Rectangle:

    """Rectangle Class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """Initialization of class rectangle
        Args:
            width of the rectangle
            height of the rctangle
        """

        type(self).number_of_instances += 1
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

    def area(self):
        """Method to get the area of rectangle
        Return:
            width * height
        """
        type(self).number_of_instances += 1
        return (self.__height * self.__width)

    def perimeter(self):
        """Method to get the perimeter of the rectangle
        Return:
            2 * (height + width)
        """
        type(self).number_of_instances += 1
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """Method to print rectangle by calling Rectangle()"""
        type(self).number_of_instances += 1
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result
        else:
            result += ("\n".join([str(self.print_symbol) * self.__width for rows in
                                  range(self.__height)]))
            return result
 
    def __repr__(self):
        """Method to return string representation"""
        type(self).number_of_instances += 1
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Method to deletes instance of class """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method to find the biggest of two rectangles"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
        