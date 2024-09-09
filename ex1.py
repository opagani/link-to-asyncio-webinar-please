#!/usr/bin/env python3

import asyncio

async def up(maximum):
    for i in range(maximum):
        print(f'up, {i}')

async def down(maximum):
    for i in range(maximum, 0, -1):
        print(f'down, {i}')

async def powers(n):
    for i in range(2, 8):
        print(f'powers, {n} ** {i} = {n**i}')
