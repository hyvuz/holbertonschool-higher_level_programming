#!/usr/bin/python3
"""Module that returns the JSON string representation of a Python object."""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
