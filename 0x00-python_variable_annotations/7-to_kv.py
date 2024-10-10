#!/usr/bin/env python3
"""This function is a type annotated function. it takes in
   a string and int or string and float as arguments and then
   returns a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """After taking in the string and int parameters
       or the string and float parameters, it returns a
       tuple with the string and the square of the number.
    """
    return (k, float(v ** 2))
