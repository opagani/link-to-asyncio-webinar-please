#!/usr/bin/env python3

# # Exercise: Task groups

# 1. Write an `async def` that takes a filename as an argument, and returns a tuple whose first element is the filename, and whose second element is a dictionary whose keys are the characters in the file, and whose values are integers describing how many times each character appears. This `async def` should iterate over the lines of the file, pausing (with `asyncio.sleep`) between each line.
# 2. From `main`, iterate over the names of several files and run our function on each of those files, each in a separate task.
# 3. Iterate over each returned value -- filename and dict, and print them out.
