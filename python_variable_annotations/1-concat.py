#!/usr/bin/env python3
"""
This module contains a type-annotated function for concatenating two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings together.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenated string of str1 and str2.
    """
    return str1 + str2
