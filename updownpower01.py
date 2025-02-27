#!/usr/bin/env python3

import asyncio

async def up(maximum):
    for i in range(maximum):
        await asyncio.sleep(0.1)
        print(f'up, {i}')

async def down(maximum):
    for i in range(maximum, 0, -1):
        await asyncio.sleep(0.1)
        print(f'down, {i}')

async def powers(n):
    for i in range(2, 8):
        await asyncio.sleep(0.1)
        print(f'powers, {n} ** {i} = {n**i}')

async def main():
    t1 = asyncio.create_task(up(10))
    t2 = asyncio.create_task(down(8))
    t3 = asyncio.create_task(powers(9))

    tasks = [t1, t2, t3]

    for one_task in tasks:
        await one_task

asyncio.run(main())
