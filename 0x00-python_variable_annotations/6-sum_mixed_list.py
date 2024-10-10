#!/usr/bin/env python3
"""This is a type-annoted function takes in a mixed
   list of integers and floats and returns their
   sum as a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ After taking in the integers and float as
        input parameters, it is set to return their
        sum as float
    """
    return float(sum(mxd_lst))
