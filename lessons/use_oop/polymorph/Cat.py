# -*- coding: utf-8 -*-
from lessons.use_oop.polymorph.Animal import Animal
from lessons.use_oop.polymorph.HomeAnimal import HomeAnimal


class Cat(Animal, HomeAnimal):

    def eat(self):
        print('Cat is eat')

    def run(self):
        print('Cat is run')

    def make_noise(self):
        print('Meow Meow!')

    def go_home(self):
        print('I\'m a Cat, I\'m going home')
