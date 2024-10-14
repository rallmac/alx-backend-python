#!/usr/bin/env python3
"""This function imports wait_random from the previous task,
   and defines an async function that takes in 2 integer arguments.
"""

import asyncio
from basic_async_syntax import wait_random  # Ensure the module name is correct


async def wait_n(n: int, max_delay: int) -> list[float]:
    """wait_n takes in 2 integers n and max_delay,
       spawns wait_random n times with max_delay and returns
       all delays sorted in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
