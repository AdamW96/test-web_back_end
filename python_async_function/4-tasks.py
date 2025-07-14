#!/usr/bin/env python3
"""
an async routine that executes multiple tasks concurrently.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay for each task_wait_random call.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    # Create a list of tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Execute all tasks concurrently and collect results
    delays = await asyncio.gather(*tasks)

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
