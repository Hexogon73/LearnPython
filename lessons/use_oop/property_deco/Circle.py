# -*- coding: utf-8 -*-

""" в Python @property используется вместо методов getter и setter
"""


class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2


if __name__ == '__main__':
    circle = Circle()
    print(f'radius= {circle.radius}, diameter= {circle.diameter}')
    circle.radius = 5
    print(f'radius= {circle.radius}, diameter= {circle.diameter}')
