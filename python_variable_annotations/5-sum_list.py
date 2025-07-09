#!/usr/bin/env python3
"""
Module contains a type-annotated function for summing a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of float numbers.

    Args:
        input_list (List[float]): A list containing float numbers to sum.

    Returns:
        float: The sum of all float numbers in the input list.
    """
    return sum(input_list)
