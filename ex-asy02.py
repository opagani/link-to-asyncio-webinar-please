#!/usr/bin/env python3

# Exercise: Task groups

# Write an async def that takes a filename as an argument, and returns a tuple whose first element is the filename,
# and whose second element is a dictionary whose keys are the characters in the file, and whose values are integers
# describing how many times each character appears. This async def should iterate over the lines of the file, pausing (with asyncio.sleep) between each line.
# From main, iterate over the names of several files and run our function on each of those files, each in a separate task.
# Iterate over each returned value -- filename and dict, and print them out.

import asyncio
import os


async def file_chars(filename):
    counts = {}

    await asyncio.sleep(0.1)
    for one_line in open(filename):
        for one_character in one_line:
            if one_character in counts:
                counts[one_character] += 1
            else:
                counts[one_character] = 1

    return filename, counts


async def main():
    dir_list = os.listdir(".")  # get a list of files in the current directory
    # create an asyncio.TaskGroup
    # we'll create this group inside of a "with"
    for one_file in dir_list:
        async with asyncio.TaskGroup() as tg:
            t1 = tg.create_task(file_chars(one_file))

            print(f"Task group for {one_file} has been created")

    # at the end of this block, we have automatically awaited all of the
    # tasks in the Task Group

    print(t1.result())  #  we can turn to the task and ask for its result


asyncio.run(main())
