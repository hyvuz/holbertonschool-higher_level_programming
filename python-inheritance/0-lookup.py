#!/usr/bin/python3
"""Module that defines a function to list attributes and methods of an obj"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing names of attributes and methods.
    """
    return dir(obj)
