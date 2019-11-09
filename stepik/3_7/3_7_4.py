"""Группа биологов в институте биоинформатики завела себе черепашку.

После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное
расстояние в сантиметрах, которое должна пройти черепашка.

Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу,
которая определит, куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу,
которая выведет точку, в которой окажется черепашка после всех команд. Для простоты они решили считать, что движение
начинается в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.

Программе подаётся на вход число команд n, которые нужно выполнить черепашке, после чего n строк с самими командами.
Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки.
Все координаты целочисленные.
"""


def run_command(current_position, direction, distance):
    if direction == 'север':
        current_position[1] += distance
    elif direction == 'запад':
        current_position[0] -= distance
    elif direction == 'юг':
        current_position[1] -= distance
    elif direction == 'восток':
        current_position[0] += distance
    else:
        raise ValueError(f'Variable "direction" should be in [север, запад, юг, восток] not "{direction}"')
    return current_position


command_count = int(input())
point = [0, 0]
for n in range(command_count):
    command = input().split()
    point = run_command(point, command[0], int(command[1]))

print(*point)
