#!/usr/bin/python3
"""finds a peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """finds a peak in list of unsorted integers"""

    pk = len(list_of_integers)

    if pk == 0:
        return None

    less = 0
    h = pk - 1

    while less < h:
        hlf = (less + h) // 2

        if list_of_integers[hlf] < list_of_integers[hlf + 1]:
            less = hlf + 1
        else:
            h = hlf

    return list_of_integers[less]
