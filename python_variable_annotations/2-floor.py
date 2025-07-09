#!/usr/bin/env python3
"""
This module contains a type-annotated function for computing the floor of a float.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a float number.

    Args:
        n (float): The float number to compute the floor of.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
