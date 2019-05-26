# -*- coding: utf-8 -*-
from lessons.use_oop.polymorph.Animal import Animal
from lessons.use_oop.polymorph.HomeAnimal import HomeAnimal


class Dog(Animal, HomeAnimal):

    def eat(self):
        print('Dog is eat')

    def run(self):
        print('Dog is run')

    def make_noise(self):
        print('Wow wow!')

    def go_home(self):
        print('I\'m a Dog, I\'m going home')
