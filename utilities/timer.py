import logging
from timeit import default_timer


def timer(func):
    def inner(*args, **kwargs):
        t1 = default_timer()
        func(*args, **kwargs)
        t2 = default_timer()
        delta = t2 - t1
        logging.info(f'RunTime: {delta=}')

    return inner
