#!/usr/bin/env python3

import asyncio
import time
import random

async def hello(number):
    await asyncio.sleep(random.randint(0, 4))  # sleep for up to 4 seconds
    print(f'[{number}] Hello!')

async def main():
    for i in range(10):
        task = asyncio.create_task(hello(i))
        await task

asyncio.run(main())
