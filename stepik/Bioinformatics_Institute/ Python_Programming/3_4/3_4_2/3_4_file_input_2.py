# https://stepik.org/lesson/3363/step/2?unit=1135

import os
import re

file_path = os.path.join('', 'dataset_3363_2.txt')
text = None
with open(file_path, 'r') as f:
    text = f.readline()

numbers = re.findall(r'\d+', text)
repl = re.sub(r'\d+', ',<num>,', text)
splited = re.split(r',', repl)

previous = ''
current = ''
result = ''
for idx, c in enumerate(splited):
    previous = current
    current = c
    if current == '<num>':
        num = int(numbers.pop(0))
        splited[idx] = num
        result += previous * num
print(result)
