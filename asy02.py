#!/usr/bin/env python3

import asyncio

async def hello():
    print('Hello!')

# to put something on the event loop, we can say asyncio.run()

asyncio.run(hello())
