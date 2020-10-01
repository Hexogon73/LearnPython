'''Создайте класс Vector, который хранит в себе вектор целых чисел.
У класса Vector есть:
1)конструктор __init__, принимающий произвольное количество аргументов.
Среди всех переданных аргументов необходимо оставить только целые числа и сохранить их в атрибут values в виде списка;
2)переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
"Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть упорядочены по возрастанию;
"Пустой вектор", если наш вектор не хранит в себе значения
'''


class Vector:
    def __init__(self, *args):
        self.values = [arg for arg in args if isinstance(arg, int)]

    def __str__(self):
        if self.values:
            return f'Вектор({", ".join([str(val) for val in sorted(self.values)])})'
        return 'Пустой вектор'


if __name__ == '__main__':
    v1 = Vector(1, 2, 3)
    print(v1)  # печатает "Вектор(1, 2, 3)"
    v2 = Vector()
    print(v2)  # печатает "Пустой вектор"
    v3 = Vector(1, 2, 3, 10)
    print(v3)  # печатает "Вектор(1, 2, 3, 10)"
