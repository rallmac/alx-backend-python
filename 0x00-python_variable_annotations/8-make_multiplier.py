#!/usr/bin/env python3
"""This function is a type annotated function that takes in
   a multiplier and serves as a function to multiply floats
   by the multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """After taking in the float multiplier, the code
       the function that multiplies its input  by
       the float multiplier
    """
    def multiplier_function(value: float) -> float:
        """This function is the input to new mutltiplier
           function to return the multiplier
        """
        return value * multiplier
    return multiplier_function
