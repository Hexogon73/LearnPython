# -*- coding: utf-8 -*-

"""
Использование интерфейса в качестве полиморфного аргумента
(Отправляем домашних животных домой, чтобы их не подстрелил охотник :))
"""

from lessons.use_oop.polymorph.Animal import Animal
from lessons.use_oop.polymorph.Cat import Cat
from lessons.use_oop.polymorph.Dog import Dog
from lessons.use_oop.polymorph.Wolf import Wolf
from lessons.use_oop.polymorph.Hunter import Hunter


class Solution(object):
    if __name__ == '__main__':
        print("--- poly_2 ---")
        print("--- HomeAnimals Polymorphysm ---")

        home_animals = list()
        home_animals.append(Dog())
        home_animals.append(Cat())

        for ha in home_animals:
            # если животное реализует интерфейс HomeAnimal то мы можем отправить его домой вызвав метод goHome()
            ha.go_home()

        print("--- Animals Polymorphysm ---")

        animals = list()

        animals.append(Dog())
        animals.append(Cat())
        animals.append(Wolf())

        hunter = Hunter()

        for animal in animals:
            animal.run()
            animal.eat()
            # animal.make_noise()
            hunter.give_shot(animal)
