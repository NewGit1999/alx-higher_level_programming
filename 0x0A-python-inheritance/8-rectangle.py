#!/usr/bin/python3
"""geometry class"""


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """initialize height and width"""
        self.integer_validator("width", width)
        self.__width == width
        self.integer_validator("height", height)
        self.__height == height
