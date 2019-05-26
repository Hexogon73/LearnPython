# -*- coding: utf-8 -*-
from abc import *


class HomeAnimal(metaclass=ABCMeta):

    @abstractmethod
    def go_home(self):
        pass
