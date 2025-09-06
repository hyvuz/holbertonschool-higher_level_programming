#!/usr/bin/python3
"""Defines a Square that supports numeric size and area-based comparisons."""


class Square:
    """Represents a square and supports comparisons based on area."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieve the size (side length)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation (int or float, >= 0)."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    # ---- Comparators based on area ----
    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
