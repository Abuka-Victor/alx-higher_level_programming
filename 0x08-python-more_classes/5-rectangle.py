#!/usr/bin/python3
"""
A simple Rectangle: Task 2
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

    def area(self):
        """

        Returns: The area of the rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """

        Returns: The perimeter of the rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """

        Returns: The string representation of a Rectangle

        """
        return_string = ""
        if not (self.__width == 0 or self.__height == 0):
            for i in range(self.__height):
                return_string += "#" * self.__width
                if i != (self.__height - 1):
                    return_string += '\n'
        return return_string

    def __repr__(self):
        """

        Returns: A Canonical representation of a Rectangle

        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        print("Bye rectangle...")
