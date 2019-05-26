# -*- coding: utf-8 -*-

""" https://proglib.io/p/python-oop/#log-in
"""


class Mammal:
    def move(self):
        print('Двигается')


class Hare(Mammal):
    def move(self):
        print('Прыгает')


animal = Mammal()
animal.move()  # Двигается
hare = Hare()
hare.move()  # Прыгает
