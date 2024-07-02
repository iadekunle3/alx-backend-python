#!/usr/bin/env python3
"""Module that contains a func for asyncio.Task"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes an integer and returns a asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))