# __str__ and __repr__

class Lion:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'The object Lion = {self.name}'

    def __str__(self):
        return f'Lion = {self.name}'


q = Lion('Bob')
print(q)

w = Lion('Vasya')
print(w)
