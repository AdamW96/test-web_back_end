#!/usr/bin/env python3
"""
A type-annotated function for summing a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):.

    Returns:
        float: The sum of all numbers in the mixed list as a float.
    """
    return sum(mxd_lst)
