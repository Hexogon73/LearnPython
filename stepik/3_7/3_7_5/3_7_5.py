# https://stepik.org/lesson/3380/step/5?unit=963
"""Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.

Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.

Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост

Класс обозначается только числом. Буквенные модификаторы не используются.
Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется
натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый).
Если про какой-то класс нет информации, необходимо вывести напротив него прочерк, например:
Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153

Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0
"""
import os
import io


class Student:
    grade_number: int
    surname: str
    height: int

    def __init__(self, grade_number, surname, height):
        self.grade_number = int(grade_number)
        self.surname = surname
        self.height = int(height)


class Grade:
    number: int
    students: list

    def __init__(self, number):
        self.number = number
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def get_middle_height(self):
        sum_height = 0
        for student in self.students:
            sum_height += student.height
        return float(sum_height / len(self.students))


input_file_path = os.path.join(os.getcwd(), 'dataset_3380_5.txt')
with io.open(input_file_path, encoding='utf-8') as file:
    text = file.readlines()

grade_list = {}

for s in text:
    grade_number, surname, height = s.strip('\n').split('\t')
    student = Student(grade_number, surname, height)
    if grade_number in grade_list.keys():
        grade_list[grade_number].add_student(student)
    else:
        grade = Grade(grade_number)
        grade.add_student(student)
        grade_list[grade_number] = grade

for i in range(1, 12):
    if str(i) in grade_list.keys():
        middle = grade_list[str(i)].get_middle_height()
        print(f'{i} {middle:.1f}')
    else:
        print(f'{i} -')
