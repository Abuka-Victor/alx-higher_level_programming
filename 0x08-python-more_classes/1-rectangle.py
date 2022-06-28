#!/usr/bin/python3
"""
A simple Rectangle: Task 1
"""


class Rectangle:
    """
    The Simple Rectangle Class
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """

        Returns: The width of the object

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle
        Args:
            value: The new width

        Returns: Null Void

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """

        Returns: The height of the object

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle
        Args:
            value: The new height

        Returns: Null Void

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
