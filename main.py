import argparse
import asyncio
import platform

from adapter.adapter import data_adapter
from api.api3 import coroutines_handler
from viewer.viewer import pretty_view

parser = argparse.ArgumentParser(description='Process some integers.', )
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
days = args.accumulate(args.integers)


def main(number: int = 2):
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    while number <= 10:
        data = asyncio.run(coroutines_handler(number))
        pretty_view(data_adapter(data))
        break
    else:
        print('Number of days to select rates should not exceed 10')


if __name__ == '__main__':
    main(days)
