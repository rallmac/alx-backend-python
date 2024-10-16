#!/usr/bin/env python3
"""Collect 10 random numbers using async
   comprehension.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers from
       async_generator.
    """
    value = [i async for i in async_generator()]
    return value
