#!/usr/bin/env python3
"""
a coroutine that measures the runtime of parallel async comprehensions.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel.

    Returns:
        float: executing four async_comprehensions in parallel.
    """
    start_time = time.time()

    # Execute four async_comprehension coroutines in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    return end_time - start_time
