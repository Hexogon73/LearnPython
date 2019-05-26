# -*- coding: utf-8 -*-
from lessons.use_oop.polymorph.Animal import Animal


class Hunter(object):
    def give_shot(self, a: Animal):
        print('Hunter shoots at in the ' + a.__class__.__name__)
        a.make_noise()
        a.run()
