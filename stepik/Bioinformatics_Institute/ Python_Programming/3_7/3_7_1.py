"""Напишите программу, которая принимает на стандартный вход список игр футбольных команд
 с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
"""


class Team:
    name: str
    count_game: int = 0
    win: int = 0
    draw: int = 0
    defeat: int = 0
    total: int = 0

    def __init__(self, name):
        self.name = name

    def get_total(self):
        self.total = sum([self.win * 3, self.draw])
        return self.total


number = int(input())
strings = []
for n in range(number):
    # Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
    strings.append(input())

result = f'{number}\n'
teams = {}
for s in strings:
    splited = s.split(';')
    team_name1, count1, team_name2, count2 = splited
    team1 = None
    team2 = None
    if team_name1 not in teams.keys():
        team1 = Team(team_name1)
        teams[team_name1] = team1
    else:
        team1 = teams[team_name1]
    if team_name2 not in teams.keys():
        team2 = Team(team_name2)
        teams[team_name2] = team2
    else:
        team2 = teams[team_name2]

    team1.count_game += 1
    team2.count_game += 1
    if count1 > count2:
        team1.win += 1
        team2.defeat += 1
    elif count1 < count2:
        team2.win += 1
        team1.defeat += 1
    else:
        team1.draw += 1
        team2.draw += 1

for name, team in teams.items():
    # Команда:Всего_игр Побед Ничьих Поражений Всего_очков
    print(f'{name}:{team.count_game} {team.win} {team.draw} {team.defeat} {team.get_total()}')
