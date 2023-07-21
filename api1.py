import asyncio
import platform

import aiohttp

from query_params import create_urls


async def get_rates(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            return await response.json()


async def main(routes):
    return await asyncio.gather(*routes)


futures = [get_rates(url) for url in create_urls(2)]

if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    result = asyncio.run(main(futures))
    # print(f'{result=}')
    for i in result:
        rates = i['exchangeRate']
        # print(i['date'], f"{rates=}")
        eur = list(filter(lambda x: x['currency'] == 'EUR', rates))[0]
        usd = list(filter(lambda x: x['currency'] == 'USD', rates))[0]
        # print(f"EUR: {eur['currency'], eur['saleRate'], eur['purchaseRate']}")
        # print(f"USD: {usd['currency'], usd['saleRate'], usd['purchaseRate']}")
        print(f'{eur=}')
        print(f'{usd=}')
