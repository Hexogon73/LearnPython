"""page 284"""
with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')
