#!/usr/bin/env python3
"""
a coroutine that uses async comprehension to collect random numbers.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect random numbers using async comprehension over async_generator.

    Returns:
    List[float]: A list containing 10 random numbers from async_generator.
    """
    return [num async for num in async_generator()]