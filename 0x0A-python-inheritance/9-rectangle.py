#!/usr/bin/python3
"""defining class Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits BaseGeometry
    """

    def __init__(self, width, height):
        """
        initialization of the class
        Args:
            width
            height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """implemented area method"""
        return (self.__height * self.__width)

    def __str__(self):
        """return [Rectangle] <width>/<height>"""
        return ("[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                          self.__width, self.__height))
