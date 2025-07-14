#!/usr/bin/env python3
"""
This module contains a function that creates asyncio Tasks.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task that wraps the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A Task object that wraps wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
