#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """write a string to a text file"""
    with open (filaname, 'w', encoding="UTF8") as f:
        return f.write(text)
