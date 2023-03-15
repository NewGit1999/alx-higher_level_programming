#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for ky in list(a_dictionary.keys()):
        del a_dictionary[ky]
    return a_dictionary
