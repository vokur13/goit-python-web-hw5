import asyncio

import aiohttp

from utilities import create_urls

currency_rate = ['EUR', 'USD']


async def fetch_currency_rates(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, ssl=False) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error status: {response.status} for {url}")
        except aiohttp.ClientConnectorError as err:
            print(f'Connection error: {url}', str(err))


async def coroutines_handler(days):
    coroutines = [fetch_currency_rates(i) for i in create_urls(days)]
    return await asyncio.gather(*coroutines)
