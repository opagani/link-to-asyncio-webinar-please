#!/usr/bin/env python3

import asyncio
import time
import random

async def hello(number):
    await asyncio.sleep(random.randint(0, 4))  # sleep for up to 4 seconds
    print(f'[{number}] Hello!')

async def main():
    # create a list of tasks that we have scheduled
    tasks = [asyncio.create_task(hello(i))
             for i in range(10)]

asyncio.run(main())
