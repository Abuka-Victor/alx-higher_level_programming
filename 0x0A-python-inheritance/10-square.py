#!/usr/bin/python3
""" Module for task 10 """
rect = __import__("9-rectangle").Rectangle


class Square(rect):
    def __init__(self, size):
        self.__size = self.integer_validator("Size", size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {size}/{size}".format(size=self.__size)
