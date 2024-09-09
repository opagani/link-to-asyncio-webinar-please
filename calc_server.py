#!/usr/bin/env python3

import asyncio

def calc(s):   # gets a string with a math expression, and returns the result
    first, op, second = s.split()

    first = int(first)
    second = int(second)

    if op == '+':
        result = first + second
    elif op == '-':
        result = first - second
    else:
        result = f'Operator {op} not supported'

    return result

async def main():
    server = await asyncio.start_server(handle_client,
                                        'localhost',
                                        6789)

    async with server:
        await server.serve_forever()
