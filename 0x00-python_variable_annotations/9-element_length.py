#!/usr/bin/env python3
""" This function takes in the length of a list
    as input and returns the length of size in
    length of the list
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """this function takes a list of strings (lst) as input
       and returns a list of tuples, where each tuple contains
       a string and its length.
    """
    return [(i, len(i)) for i in lst]
