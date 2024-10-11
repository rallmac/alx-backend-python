#!/usr/bin/env python3
"""This module contains a function to zoom in on
   elements of a tuple by a given factor.
"""


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in on elements of the tuple by repeating
       each element 'factor' times. it takes in tupple
       as input containing elements be zoomed and returns
       a list containig the zoomed in elements
    """
    zoomed_in: List = [
            item for item in lst
            for i in range(factor)
    ]
    return zoomed_in
