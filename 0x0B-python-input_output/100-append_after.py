#!/usr/bin/python3
"""insert and update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file"""
    with open(filename, 'r') as f:
        data = f.readlines()
    with open(filename, 'w') as f:
        for a in data:
            if search_string in a:
                f.write(a + new_string)
            else:
                f.write(a)
