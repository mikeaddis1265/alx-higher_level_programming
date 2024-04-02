#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines
    a square with private instance attribute
     """

    def __init__(self, size=0):
        try:
            if isinstance(size) == int:
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer\n")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = size
