#!/usr/bin/env python3
""" This function defines the type of variable that
    represents the type of values in the dictionary
    and the default value
"""

from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """This module takes in dictionary with keys of any
       type and any value and key of any type and default
       value and returns a value of any type
    """
    if Key in dct:
        return dct[key]
    else:
        return defult
