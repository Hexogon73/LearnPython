"""page 539"""
import pprint
from datetime import datetime


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M:%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
fts = {convert2ampm(k): v.title() for k, v in flights.items()}
pprint.pprint(fts)

dests = set(fts.values())
wests = {k: v for k, v in fts.items() if v == 'West End'}

for dest in dests:
    print(dest, '->', [k for k, v in fts.items() if v == dest])

# page 537
when = {}
for dest in dests:
    when[dest] = [k for k, v in fts.items() if v == dest]
pprint.pprint(('when=', when))

when2 = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
pprint.pprint(('when2=', when2))

for i in [x * 3 for x in [1, 2, 3, 4, 5]]:  # генератор списка
    print(i, end=' ')

print()

for i in (x * 3 for x in [1, 2, 3, 4, 5]):  # выражение-генератор
    print(i, end=' ')
