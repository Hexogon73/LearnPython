# -*- coding: utf-8 -*-
from lessons.use_oop.polymorph.Animal import Animal


class Wolf(Animal):

    def eat(self):
        print('Wolf is eat')

    def run(self):
        print('Wolf is run')
