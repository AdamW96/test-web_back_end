#!/usr/bin/env python3
"""
an async generator that yields random numbers.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async generator that yields random numbers between 0 and 10.

    Loops 10 times, each time asynchronously waits 1 second,
    then yields a random float between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
