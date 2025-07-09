#!/usr/bin/env python3
"""
A type-annotated function that creates a tuple from a string and a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a number.

    Args:
        k (str): first element
        v (Union[int, float]): second element

    Returns:
        Tuple[str, float]: first element is the string k
                          second element is the square of v as a float.
    """
    return k, float(v * v)
