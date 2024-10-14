#!/usr/bin/env python3
"""This is an asynchronous coroutine that takes in an integer argument
   waits for a random delay and eventually returns it
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait_random takes in max_delay, waits for a random
       float value seconds and returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
