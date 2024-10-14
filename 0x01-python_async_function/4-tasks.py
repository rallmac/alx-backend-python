#!/usr/bin/env python3
"""This module defines a function to create multiple
   asyncio Tasks for wait_random.
"""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """task_wait_n takes in 2 integers n and max_delay,
       spawns task_wait_random n times with max_delay and returns
       all delays sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
