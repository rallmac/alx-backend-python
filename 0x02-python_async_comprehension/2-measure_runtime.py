#!/usr/bin/env python3
"""Measure runtime of async_comprehension executed
   in parallel.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Measures the total runtime of running async_comprehension
       four times in parallel.
    """
    start_time = time.perf_counter()  # Start measuring time
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.perf_counter()  # End measuring time
    return end_time - start_time  # Return the total runtime
