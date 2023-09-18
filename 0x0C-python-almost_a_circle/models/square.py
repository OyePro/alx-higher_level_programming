#!/usr/bin/python3
"""defining Class Square which inherits Class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializing...
        Args:
            size, x, y, id
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getting the value of size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """setting the value of size"""
        self.width = value
        self.height = value

    """def area(self):"""
    """
        method to print area of square
        """
    """return ((self.size)**2)"""

    def display(self):
        """
        method to print square in form of #
        to standard output
        """
        print("\n" * self.y, end="")
        print("\n".join([" " * self.x + "#" * self.size
                         for i in range(self.size)]))

    def __str__(self):
        """
        printing square in format:
        [Square] (<id>) <x>/<y> - <size>
        """
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}"
                .format(self.__class__.__name__, self.id, self.x,
                        self.y, self.size))

    def update(self, *args, **kwargs):
        """
        method to update Square and assigns an argument
        (keywords or non keywords) to its attributes
        if non keywords exist, keywords will be skipped
        """
        if args:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                if index == 1:
                    self.size = arg
                if index == 2:
                    self.x = arg
                if index == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square
        """
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["size"] = self.size
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return (my_dict)
