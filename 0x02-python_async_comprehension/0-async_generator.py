#!/usr/bin/env python3
"""This module contains an asynchronous
   generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields random numbers between 0 and 10
       with a 1-second delay, 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
