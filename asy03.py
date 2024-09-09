#!/usr/bin/env python3

import asyncio
import time

async def hello():

    # if something is going to take a long time, then I should say "await"
    # that will allow another coroutine to run instead of us
    await time.sleep(1)
    print('Hello!')

# to put something on the event loop, we can say asyncio.run()

asyncio.run(hello())
