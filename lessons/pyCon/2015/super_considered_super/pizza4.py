from .pizza2 import Pizza, DoughFactory

"""18:33"""


class OrganicDoughFactory(DoughFactory):

    def get_dough(self):
        return 'organic dough'


class OrganicPizza(Pizza, OrganicDoughFactory):
    pass


if __name__ == '__main__':
    OrganicPizza().order_pizza('Sausage', 'Mushroom')
