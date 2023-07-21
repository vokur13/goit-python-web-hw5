import asyncio
import platform

import aiohttp

from query_params import create_urls


async def main(number):
    async with aiohttp.ClientSession() as session:
        for url in create_urls(number):
            try:
                async with session.get(url, ssl=False) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        print(f"Error status: {response.status} for {url}")
            except aiohttp.ClientConnectorError as err:
                print(f'Connection error: {url}', str(err))


# def data_adapter(data: dict):
#     return [{f"{el.get('ccy')}": {"buy": float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]

def data_adapter(data: dict):
    return data


if __name__ == '__main__':
    # t1 = default_timer()
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    data = asyncio.run(main(2))
    print(f'{data=}')
    print(f'{data_adapter(data)=}')
    # t2 = default_timer()
    # delta = t2 - t1
    # print(f"Runtime {delta=}")
