#!/usr/bin/python3
"""defining function inherits_from"""


def inherits_from(obj, a_class):
    """
    Return a bool if obj inherits directly or indirectly.
    type() is use for getting specific class
    isinstance() for getting class and parent class. takes two
    arguments, the object and the class
    issubclass() for getting the subclass which object belongs as the
    name implies
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
 