# -*- coding: utf-8 -*-
class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Init {})'.format(self.name))

        Robot.population += 1

    def __del__(self):
        print('{} destroying!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} has been last.'.format(self.name))
        else:
            print('Ostalos {0:d} worked robots.'.format(Robot.population))

    def say_hi(self):
        print('Hi! My senior named me {}.'.format(self.name))

    @staticmethod
    def how_many():
        print('We have {0:d} robots.'.format(Robot.population))


droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

print('\n here robots have work \n')
print('robots finish your work. Destroy him.')
del droid1
del droid2

Robot.how_many()
