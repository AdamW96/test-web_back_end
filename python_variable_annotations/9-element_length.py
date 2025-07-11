#!/usr/bin/env python3
"""
A type-annotated function that returns the length of elements in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences
                                 (like strings, lists, tuples, etc.)

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
                                   the original sequence and its length.
    """
    return [(i, len(i)) for i in lst]
