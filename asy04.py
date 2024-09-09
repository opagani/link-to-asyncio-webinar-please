#!/usr/bin/env python3

import asyncio
import time

async def hello():
    await asyncio.sleep(1)
    print('Hello!')

async def main():
    print('Before await')
    await hello()    # a coroutine is awaitable!
    print('After await')

asyncio.run(main())
