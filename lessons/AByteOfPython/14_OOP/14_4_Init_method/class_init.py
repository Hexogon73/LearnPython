# -*- coding: utf-8 -*-
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hi! My name is', self.name)


p = Person('Serg')
p.say_hi()
