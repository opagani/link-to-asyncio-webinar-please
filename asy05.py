#!/usr/bin/env python3

import asyncio
import time

async def hello():
    print('[hello] Before sleep')
    await asyncio.sleep(1)
    print('[hello] After sleep')
    print('Hello!')
    print('[hello] After print sleep')

async def main():
    print('[main] Before await')
    await hello()    # a coroutine is awaitable!
    print('[main] After await')

asyncio.run(main())
