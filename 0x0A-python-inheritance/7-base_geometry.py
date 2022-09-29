#!/usr/bin/python3
"""Defining class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """
        method area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(name) is str:
            self.name = name
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        self.value = value
