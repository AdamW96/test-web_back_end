#!/usr/bin/env python3
"""
An async routine that executes multiple coroutines concurrently.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    # Create a list of coroutines
    coroutines = [wait_random(max_delay) for _ in range(n)]

    # Execute all coroutines concurrently and collect results
    delays = await asyncio.gather(*coroutines)

    # Return delays in ascending order without using sort()
    # We'll manually insert each delay in the correct position
    result = []
    for delay in delays:
        # Find the correct position to insert this delay
        inserted = False
        for i in range(len(result)):
            if delay < result[i]:
                result.insert(i, delay)
                inserted = True
                break
        if not inserted:
            result.append(delay)

    return result
