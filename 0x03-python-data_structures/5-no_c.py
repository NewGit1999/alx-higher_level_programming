#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for character in range (len(my_string)):
        if my_string[character] != 'c' and my_string[character] != 'C':
            new_string += my_string[character]
    return new_string
