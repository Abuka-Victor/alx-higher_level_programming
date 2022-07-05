#!/usr/bin/python3
""" My module for task 8 """

base = __import__('7-base_geometry').BaseGeometry


class Rectangle(base):

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
