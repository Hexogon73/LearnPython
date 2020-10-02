class DoughFactory(object):

    def get_dough(self):
        return 'dough'


class Pizza(DoughFactory):

    def order_pizza(self, *toppings):
        print('Getting dough')
        dough = DoughFactory().get_dough()
        print(f'Making pie with {dough}')
        for topping in toppings:
            print(f'Adding: {topping}')


if __name__ == '__main__':
    Pizza().order_pizza('Pepperoni', 'Bell Pepper')
