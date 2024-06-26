#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:

    """Initialization of an instance object"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """delete an obj instance"""
    def __del__(self):
        print("Bye rectangle...")

    @property
    def height(self):
        """Return the size"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Return the size"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """return area"""
        return self.__height * self.__width

    def perimeter(self):
        """return perimeter of rectangle"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """ return the rectangle with the character #
        """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
