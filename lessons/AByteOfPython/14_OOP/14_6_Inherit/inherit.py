# -*- coding: utf-8 -*-
class SchoolMember:
    """Base class people in school"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Created SchoolMember: {})'.format(self.name))

    def tell(self):
        print('Name: "{}" Age: "{}"'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    """Teacher"""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Created Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    """Student"""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Created Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{0:d}"'.format(self.marks))


t = Teacher('Mr. Teacher', 40, 30000)
s = Student('Serg', 25, 75)
m = SchoolMember('sm', 10)

print()

members = [t, s, m]
for member in members:
    member.tell()
