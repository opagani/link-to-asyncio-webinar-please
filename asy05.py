#!/usr/bin/env python3

import asyncio
import time

async def hello(number):
    await asyncio.sleep(random.randint(0, 4))  # sleep for up to 4 seconds
    print(f'[{number}] Hello!')

async def main():
    await hello()    # a coroutine is awaitable!

asyncio.run(main())
