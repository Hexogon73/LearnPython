"""page 533"""
# 1
data = list(range(1, 9))
events = []
for num in data:
    if not num % 2:
        events.append(num)
print(events)

events = [num for num in data if not num % 2]
print(events)

# 2
data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)
print(words)

words = [num for num in data if isinstance(num, str)]
print(words)

# 3
data = list('So long and thanks for all the fish'.strip())
title = []
for word in data:
    title.append(word.title())
print(title)
title = [word.title() for word in data]
print(title)
