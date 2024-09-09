#!/usr/bin/env python3

# I want to iterate over a list of URLs, and retrieve each one,
# counting the number of bytes on that page, and then print it out.

all_urls = ['https://python.org',
        'https://pypi.org',
        'https://postgresql.org']

async def get_one_url(url, session):
    async with session.get(url) as response:
        bytes = await response.text()
        return url, len(bytes)

async def get_all_urls(urls):
    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(get_one_url(one_url))
                     for one_url in all_urls]

    for one_task in tasks:
        print(one_task.result())

async def main():
    await get_all_urls(all_urls)

asyncio.run(main())
