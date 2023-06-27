#!/usr/bin/python3
"""Define a class Square."""


class Square():
    """reresent Square"""

    __size = None

    def __init__(self, size):
            if type(size) is int:
                 raise TypeError("size must be an integer")
            if size < 0:
                 raise ValueError("size must be >= 0")
            self.__size = size
