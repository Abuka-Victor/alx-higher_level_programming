#!/usr/bin/python3
""" Module for task 7 """


class BaseGeometry:
    """ My base geometry class """

    def area(self):
        """ Calculates area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer Validator Method """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
