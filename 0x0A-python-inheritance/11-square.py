#!/usr/bin/python3
""" Module for task 10 """


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
        return value


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {width}/{height}".format(width=self.__width, height=self.__height)


class Square(Rectangle):
    def __init__(self, size):
        self.__size = self.integer_validator("Size", size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {size}/{size}".format(size=self.__size)
