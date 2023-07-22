import asyncio
from concurrent.futures import ThreadPoolExecutor
from os import cpu_count
from timeit import default_timer

import requests

from utilities.query_params import create_urls

urls = create_urls(2)

max_workers = cpu_count()


def preview_fetch(url):
    r = requests.get(url)
    return r.json()


async def preview_fetch_async():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(max_workers) as pool:
        futures = [loop.run_in_executor(pool, preview_fetch, url) for url in urls]
        result = await asyncio.gather(*futures, return_exceptions=True)
        return result


if __name__ == '__main__':
    t1 = default_timer()
    r = asyncio.run(preview_fetch_async())
    print(r)
    t2 = default_timer()
    delta = t2 - t1
    print(f"Runtime {delta=}")
