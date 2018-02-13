from lessons.use_oop.first_class import A

a = A()
b = A()
a.arg = 1  # у экземпляра a появился атрибут arg, равный 1
b.arg = 2  # а у экземпляра b - атрибут arg, равный 2
print(a.arg)
print(b.arg)
