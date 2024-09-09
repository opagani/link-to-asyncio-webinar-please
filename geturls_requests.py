#!/usr/bin/env python3

# I want to iterate over a list of URLs, and retrieve each one,
# counting the number of bytes on that page, and then print it out.

import requests
import time

all_urls = ['https://python.org',
            'https://pypi.org',
            'https://postgresql.org',
            'https://nytimes.com',
            'https://washingtonpost.com',
            'https://cnn.com']

start_time = time.time()

output = {}

for one_url in all_urls:
    print(one_url)
    r = requests.get(one_url)
    output[one_url] = len(r.content())

end_time = time.time()

print(f'Total time = {(end_time - start_time):0.2f}')
