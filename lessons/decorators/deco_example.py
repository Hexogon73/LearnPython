# -*- coding: utf-8 -*-

from datetime import datetime

""" Decorator example
https://youtu.be/Ss1M32pp5Ew
"""


def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func()
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


f1 = function1()
f2 = function2()
