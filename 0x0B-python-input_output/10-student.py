#!/usr/bin/python3
"""Defining a class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialization
        Args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if attrs is not None:
            dic = {}
            for i in attrs:
                if hasattr(self, i):
                    dic[i] = getattr(self, i)
            return (dic)
        return (self.__dict__)
