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
    return f'Done with down'

async def powers(n):
    for i in range(2, 8):
        await asyncio.sleep(0.1)
        output.append(f'powers, {n} ** {i} = {n**i}')
    return f'Done with powers'

async def main():
    # create an asyncio.TaskGroup
    # we'll create this group inside of a "with"
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(up(10))
        t2 = tg.create_task(down(8))
        t3 = tg.create_task(powers(9))

    # at the end of this block, we have automatically awaited all of the
    # tasks in the Task Group

    print(t1.result())          #  we can turn to the task and ask for its result
    print(t2.result())
    print(t3.result())


asyncio.run(main())
print(output)
