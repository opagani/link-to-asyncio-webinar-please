#!/usr/bin/env python3

# Exercise: async tasks

# Define three coroutine functions:
# up takes a single integer, maximum, and returns a string saying up and the current number. With each iteration, it'll go from 0 up to maximum.
# down is the same thing, but starts with maximum, and goes down to 0.
# powers takes a number, n, and returns (with each iteration) n to a new power up to 7 (i.e., n ** 7).
# Write a main routine that schedules them all on the event loop as tasks
# await all of them, and we should see their results intertwined.

import asyncio
import random


async def up(maximum):
    for i in range(maximum):
        await asyncio.sleep(random.randint(0, 4))
        print(f"up: {i}")


async def down(maximum):
    for i in range(maximum, -1, -1):
        await asyncio.sleep(random.randint(0, 4))
        print(f"down: {i}")


async def power():
    for i in range(8):
        await asyncio.sleep(random.randint(0, 4))
        print(f"power: {i}")


async def hello(number):
    await asyncio.sleep(random.randint(0, 4))  # sleep for up to 4 seconds
    print(f"[{number}] Hello!")


async def main():
    # create a list of tasks that we have scheduled
    tasks = [asyncio.create_task(hello(i)) for i in range(10)]

    # after we have scheduled these tasks, we'll now await them,
    # one at a time
    for one_task in tasks:
        await one_task


asyncio.run(main())
