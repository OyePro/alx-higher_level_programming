#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    li = list_of_integers
    fst = 0
    last = len(li) - 1

    if li[fst] > li[fst+1]:
        return li[fst]
    if li[last] > li[last-1]:
        return li[last]

    mid = (fst + last) // 2
    if li[mid] > li[mid-1] and li[mid] > li[mid+1]:
        return li[mid]
    if li[mid] < li[mid-1]:
        return find_peak(li[fst:mid+1])
    elif li[mid] < li[mid+1]:
        return find_peak(li[mid:last+1])
    else:
        return li[fst]
