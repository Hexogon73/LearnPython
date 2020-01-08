"""page 514..518"""
# import os

# os.chdir('lessons/HeadFirst_Python/Chapter_12_Advanced_iterations/buzzers.csv')
with open('buzzers.csv') as raw_data:
    print(raw_data.read())

import csv

with open('buzzers.csv') as data:
    for line in csv.reader(data):
        print(line)

with open('buzzers.csv') as data:
    for line in csv.DictReader(data):
        print(line)

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
print(flights)

import pprint

pprint.pprint(flights)
