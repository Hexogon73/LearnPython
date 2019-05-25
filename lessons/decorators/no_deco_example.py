# -*- coding: utf-8 -*-

from datetime import datetime


def function1(n=10000):
    start = datetime.now()
    numbers = []
    for i in range(n):
        if i % 2 == 0:
            numbers.append(i)
    print(datetime.now() - start)
    return numbers


def function2(n=10000):
    start = datetime.now()
    numbers = [i for i in range(n) if i % 2 == 0]
    print(datetime.now() - start)
    return numbers


f1 = function1()
f2 = function2()
