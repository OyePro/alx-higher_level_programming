#!/usr/bin/python3
"""
defining class Rectangle
it inherits class Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing
        Args:
            width, height, x, y, id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getting the value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setting the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getting the value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setting the height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getting the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """setting the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getting the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """setting the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method to return area of rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """method to prints retangle in form of
        # to the stdout
        """
        print("\n" * self.__y, end="")
        print("\n".join([" " * self.__x + "#" * self.__width
                         for i in range(self.__height)]))

    def __str__(self):
        """printing rectangle in format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}"
                .format(self.__class__.__name__, self.id, self.__x,
                        self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        methods to update Rectangle and assigns an argument
        (keywords or non keywords) to its attributes
        """
        if args:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                if index == 1:
                    self.width = arg
                if index == 2:
                    self.height = arg
                if index == 3:
                    self.x = arg
                if index == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["width"] = self.width
        my_dict["height"] = self.height
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return (my_dict)
