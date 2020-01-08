"""page 524"""
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

pprint.pprint(flights)
print()

flights2 = {}
for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()

pprint.pprint(flights2)

# use generators
destinations = []
for dest in flights.values():
    destinations.append(dest.title())

more_dests = [dest.title() for dest in flights.values()]
pprint.pprint(('more_dests=', more_dests))
fts2 = [convert2ampm(ft) for ft in flights.keys()]
pprint.pprint(('fts2=', fts2))
# page 530
more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}
pprint.pprint(('more_flights=', more_flights))
# page 531
just_freeport = {}
for k, v in flights.items():
    if v == 'FREEPORT':
        just_freeport[convert2ampm(k)] = v.title()
pprint.pprint(('just_freeport=', just_freeport))

just_freeport2 = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}
pprint.pprint(('just_freeport2=', just_freeport2))

just_freeport3 = {convert2ampm(k): v.title()
                  for k, v in flights.items()
                  if v == 'FREEPORT'}
pprint.pprint(('just_freeport3=', just_freeport3))
