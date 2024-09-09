#!/usr/bin/env python3

import asyncio
import time

async def hello():
    await asyncio.sleep(1)
    print('Hello!')

async def main():
    await hello()    # a coroutine is awaitable!

asyncio.run(main())
