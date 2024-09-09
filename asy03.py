#!/usr/bin/env python3

import asyncio
import time

async def hello():
    time.sleep(1)
    print('Hello!')

# to put something on the event loop, we can say asyncio.run()

asyncio.run(hello())
