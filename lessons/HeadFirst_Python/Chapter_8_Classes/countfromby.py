"""page 348..369"""


class CountFromBy:
    def __init__(self, val: int = 0, increment: int = 1) -> None:
        self.val = val
        self.incr = increment

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)


a = CountFromBy()
b = CountFromBy()

c = CountFromBy()
print(c)
c.increase()
c.increase()
c.increase()
print(c)

d = CountFromBy(100)
print(d)
d.increase()
d.increase()
d.increase()
print(d)

e = CountFromBy(100, 10)
print(e)
for i in range(3):
    e.increase()
print(e)

f = CountFromBy(increment=15)
print(f)
for i in range(3):
    f.increase()
print(f)

print(type(f))
print(id(f))
print(hex(id(f)))
