from collections import Counter, OrderedDict

"""Правила алгоритма линеаризации:
- дети вызываются раньше родителей
- родители вызываются в порядке перечисления
"""


class OrderedCounter(Counter, OrderedDict):
    def __repr__(self):
        return f'{self.__class__.__name__}({OrderedDict(self)})'

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


oc = OrderedCounter('abracadabra')
print(oc)

help(Counter)
help(OrderedCounter)
