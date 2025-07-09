#!/usr/bin/env python3
"""
a type-annotated function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value

    Returns:
        Callable[[float], float]: takes a float and returns
            the product of that float and the multiplier.
    """

    def multiply(value: float) -> float:
        """
        Multiply a value by the multiplier.

        Args:
            value (float): The value to multiply.

        Returns:
            float: The product of value and multiplier.
        """
        return value * multiplier

    return multiply
