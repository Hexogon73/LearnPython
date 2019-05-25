# -*- coding: utf-8 -*-

from datetime import datetime

""" Decorator example
https://youtu.be/Ss1M32pp5Ew
"""


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result

    return wrapper


@timeit
def function1(n=10000):
    numbers = []
    for i in range(n):
        if i % 2 == 0:
            numbers.append(i)
    return numbers


@timeit
def function2(n=10000):
    numbers = [i for i in range(n) if i % 2 == 0]
    return numbers


f1 = function1
a = f1(10)
print(a)

l1 = timeit(f1)
print(type(l1), l1.__name__)

l1 = timeit(function1)(10)  # => wrapper(10)
