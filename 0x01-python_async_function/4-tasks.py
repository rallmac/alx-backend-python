#!/usr/bin/env python3
"""Concurrent tasks with task_wait_random."""
import asyncio
from typing import List

task_wait_random = __import__('1-concurrent_coroutines').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with max_delay and
       return list of delays in ascending order.
    """
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(asyncio.create_task(task))

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
