#!/usr/bin/env python3

import asyncio

output = []

async def up(maximum):
    for i in range(maximum):
        await asyncio.sleep(0.1)
        output.append(f'up, {i}')
    return f'Done with up'

async def down(maximum):
    for i in range(maximum, 0, -1):
        await asyncio.sleep(0.1)
        output.append(f'down, {i}')

async def powers(n):
    for i in range(2, 8):
        await asyncio.sleep(0.1)
        output.append(f'powers, {n} ** {i} = {n**i}')

async def main():
    t1 = asyncio.create_task(up(10))
    t2 = asyncio.create_task(down(8))
    t3 = asyncio.create_task(powers(9))

    tasks = [t1, t2, t3]

    for one_task in tasks:
        await one_task

    print(t1.result())          #  we can turn to the task and ask for its result
    print(t2.result())
    print(t3.result())


asyncio.run(main())
print(output)
