#!/usr/bin/env python3

import asyncio
import time

async def hello():

    # if something is going to take a long time, then I should say "await"
    # that will allow another coroutine to run instead of us


    # the object to the right of await must be "awaitable"
    # most builtin Python objects and methods are *NOT* awaitable
    # await time.sleep(1)
    await asyncio.sleep(1)      # we have to use the special asyncio version of sleep, which is awaitable
    print('Hello!')

# to put something on the event loop, we can say asyncio.run()

asyncio.run(hello())
