#!/usr/bin/env python3

import asyncio
import glob

async def filechars(filename):
    output = {}
    for one_line in open(filename):
        await asyncio.sleep(0.0001)
        for one_character in one_line:
            if one_character in output:  # you could also use a defaultdict here
                output[one_character] += 1
            else:
                output[one_character] = 1
    return filename, output

async def main():
    all_filenames = glob.glob('/etc/*')

    async with asyncio.TaskGroup() as tg:
        all_tasks = [tg.create_task(filechars(one_filename))
                     for one_filename in all_filenames]

    for one_task in all_tasks:
        try:
            filename, result = one_task.result()
            print(filename)
            for key, value in result.items():
                print(f'{key}: {value}')
        except Exception:
            print(f'There was a problem')


asyncio.run(main())
