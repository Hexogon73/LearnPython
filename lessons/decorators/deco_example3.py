# -*- coding: utf-8 -*-

from datetime import datetime

""" Parameterized decorator example
https://youtu.be/Ss1M32pp5Ew
"""


def timeit(arg):
    print(arg)

    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result

        return wrapper

    return outer


@timeit('name')
def function1(n=10000):
    numbers = []
    for i in range(n):
        if i % 2 == 0:
            numbers.append(i)
    return numbers


@timeit('name')
def function2(n=10000):
    numbers = [i for i in range(n) if i % 2 == 0]
    return numbers


l1 = timeit('name')(function1)(10)

f1 = function1
a = f1(10)
print(a)
