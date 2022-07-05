#!/usr/bin/python3
""" Module for task 4 """


def inherits_from(obj, a_class):
    """ is an instance of a class that inherits  """
    return issubclass(type(obj), a_class) and type(obj) != a_class
