#!/usr/bin/env python3
"""Measure runtime of async_comprehension executed
   in parallel.
"""
import asyncio
import time


from importlib import import_module as obi


async_comprehension = obi('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of running async_comprehension
       four times in parallel.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time  # Return the total runtime
