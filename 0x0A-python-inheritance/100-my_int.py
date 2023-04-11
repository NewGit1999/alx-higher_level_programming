#!/usr/bin/python3
"""integer class"""


class MyInt:
    """integer class"""

    def __eq__(self, func):
        """opposite of what default implementation returnd"""
        if int.__ne__(self, func):
            return True
        else:
            return False

    def __ne__(self, func):
        """opposite of defualt implementation"""
        if int.__eq__(self, func):
            return True
        else:
            return False
