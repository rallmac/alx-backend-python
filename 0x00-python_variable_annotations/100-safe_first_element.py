#!/usr/bin/env python3
"""This function takes in a sequence of any value as input
   and returns any value. Optional annotation
"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """If the sequence is list, function returns list
       but if the sequence is not list, function returns
       none
    """
    if lst:
        return lst[0]
    else:
        return None
