# -*- coding: utf-8 -*-
def countdown(n: int):
    result = []
    while n != 0:
        result.append(n - 1)
        n -= 1
    return result


print(countdown(4))


# using yield
print('using yield')


def gen_countdown(n: int):
    while n != 0:
        yield n - 1
        n -= 1


g = gen_countdown(4)
print(next(g))
print(next(g))
print(next(g))

for e in gen_countdown(4):
    print(e)
