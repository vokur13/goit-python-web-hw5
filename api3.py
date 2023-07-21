import asyncio
import platform
import pprint

import aiohttp

from query_params import create_urls

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


async def main(days):
    coroutines = [fetch_currency_rates(i) for i in create_urls(days)]
    return await asyncio.gather(*coroutines)


def data_adapter(data: list):
    x_rates_list = []
    data_dict = {}
    for item in data:
        date = item.get('date')
        rates = item.get('exchangeRate')

        value_dict = {}
        for value in rates:

            if value['currency'] in currency_rate:
                value_dict.update({value['currency']: {
                    'sale': round(value['saleRate'], 2),
                    'purchase': round(value['purchaseRate'], 2)
                }})
        data_dict.update({date: value_dict})
        x_rates_list.append({date: value_dict})
    return x_rates_list


def pretty_view(data):
    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False, depth=None, compact=True)
    pp.pprint(data)


def start_app(days):
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    data = asyncio.run(main(days))
    pretty_view(data_adapter(data))
