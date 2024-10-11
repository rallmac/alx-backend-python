#!/usr/bin/env python3
"""This module contains a function to zoom in on
   elements of a tuple by a given factor.
"""


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> list:
    zoomed_in: List = [
            item for item in lst
            for i in range(factor)
            ]
    """Zooms in on elements of the tuple by repeating
       each element 'factor' times. it takes in tupple
       as input containing elements be zoomed and returns
       a list containig the zoomed in elements
    """
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
