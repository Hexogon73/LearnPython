"""page 427"""


def my_func(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()


my_func(10)
my_func(10, 20, 'str', 30)

values = [1, 2, 10, 20, 'str', 30]
my_func(values)
my_func(*values)


def my_func2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()


my_func2(a=10, b=20)
my_func2()
my_func2(a=10, b=20, c=30, d=40)


def my_func3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()


my_func3()
my_func3(10, 20, 'str', 30)
my_func3(a=10, b=20)
my_func3(1, 2, 3, a=10, b=20, c=30, d=40)
