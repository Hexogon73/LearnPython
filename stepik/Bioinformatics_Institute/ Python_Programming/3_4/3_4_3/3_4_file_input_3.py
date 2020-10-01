# https://stepik.org/lesson/3363/step/3?unit=1135

import os

file_path = os.path.join('', 'dataset_3363_3.txt')
text = ''
with open(file_path, 'r') as f:
    all_text = f.readlines()
    for s in all_text:
        text += s.lower()

splited = text.split()
print(splited)

count = 0
count_list = {}
for s in splited:
    count_list[s] = splited.count(s)
print(count_list)

max_k = ''
max_v = 0
for k, v in count_list.items():
    if v > max_v:
        max_v = v
        max_k = k
print(max_k, max_v)
