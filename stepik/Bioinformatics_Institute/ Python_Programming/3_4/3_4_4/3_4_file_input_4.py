# https://stepik.org/lesson/3363/step/4?unit=1135

"""Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
 где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку
 по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку
 по всем абитуриентам.

В качестве ответа на задание прикрепите полученный файл со средними оценками.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split
"""

import codecs
import io
import os


class Student:
    surname: str
    grading_in_mathematics: int
    grading_in_physics: int
    grading_in_russian: int

    def __init__(self, surname, grading_in_mathematics, grading_in_physics, grading_in_russian):
        self.surname = surname
        self.grading_in_mathematics = int(grading_in_mathematics)
        self.grading_in_physics = int(grading_in_physics)
        self.grading_in_russian = int(grading_in_russian)

    def get_middle(self):
        middle = (self.grading_in_mathematics + self.grading_in_physics + self.grading_in_russian) / 3
        return middle

    def show_middle(self):
        print(self.get_middle())


input_file_path = os.path.join(os.getcwd(), 'dataset_3363_4.txt')
print(input_file_path)
text = ''
with io.open(input_file_path, encoding='utf-8') as file:
    all_text = file.readlines()

students = []
for string in all_text:
    students.append(Student(*string.split(';')))

result = []
sum_grading_in_mathematics = 0
sum_grading_in_physics = 0
sum_grading_in_russian = 0
for student in students:
    result.append(student.get_middle())
    sum_grading_in_mathematics += student.grading_in_mathematics
    sum_grading_in_physics += student.grading_in_physics
    sum_grading_in_russian += student.grading_in_russian

result.append('{} {} {}'.format(sum_grading_in_mathematics / len(students),
                                sum_grading_in_physics / len(students),
                                sum_grading_in_russian / len(students)))

output_file_path = os.path.join(os.getcwd(), 'output.txt')
with codecs.open(output_file_path, 'w', 'utf-8') as file:
    for line in result:
        file.write(str(line) + '\n')
