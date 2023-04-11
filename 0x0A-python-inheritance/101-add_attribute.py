#!/usr/bin/python3
"""new attribute"""


def add_attribute(obj, name, value):
    """add new attribute to an object"""
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
