#!/usr/bin/env python3

import asyncio
import time

async def hello():
    await asyncio.sleep(1)
    print('Hello!')

asyncio.run(hello())
