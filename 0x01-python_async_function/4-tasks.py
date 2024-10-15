#!/usr/bin/env python3
"""This module defines a function to create multiple
   asyncio Tasks for wait_random.
"""

import asyncio
from typing import List


task_wait_random = __import__('1-concurrent_coroutines').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n takes in 2 integers n and max_delay,
       spawns task_wait_random n times with max_delay and returns
       all delays sorted in ascending order.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
