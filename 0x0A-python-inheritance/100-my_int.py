#!/usr/bin/python3
"""integer class"""


class MyInt:
    """integer class"""

    def __eq__(self, func):
        """opposite of what default implementation returnd"""
        return super().__ne__(func)

    def __ne__(self, func):
        """opposite of defualt implementation"""
        return super().__eq__(func)
