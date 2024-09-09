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

async def handle_client(reader, writer):
    print(f'Got a connection; {reader=} and {writer=}')

    while True:
        client_bytes = await reader.read(255)
        client_string = client_bytes.decode('utf-8').strip()
        print(f'Got {client_string=}')

        if not client_string:
            break

        result = calc(client_string)
        writer.write(result.encode())
        await writer.drain()

async def main():
    server = await asyncio.start_server(handle_client,
                                        'localhost',
                                        6789)

    async with server:
        await server.serve_forever()

asyncio.run(main())
