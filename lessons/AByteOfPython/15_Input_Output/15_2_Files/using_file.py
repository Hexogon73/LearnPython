# -*- coding: utf-8 -*-
poem = '''\
Programming is fun,
If work is sun
using Python!
'''

f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end=' ')

f.close()
