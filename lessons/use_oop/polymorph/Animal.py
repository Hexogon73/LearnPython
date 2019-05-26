# -*- coding: utf-8 -*-
from abc import *


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def eat(self):
        print('Animal is eat')

    @abstractmethod
    def run(self):
        print('Animal is run')

    def make_noise(self):
        print('Rrrr!')
