print("Задание 1")
white = '\u001b[47m'
blue = "\u001b[44m"
end = "\u001b[0m"
for i in range(2):
    print(f'{white}{" " * 7}{blue} {" " * 2}{white}{" " * 11}{end}')
print(f'{blue} {" " * 20}{end}')
for i in range(2):
    print(f'{white}{" " * 7}{blue} {" " * 2}{white}{" " * 11}{end}')


print("Задание 2")
black = '\u001b[40m'
white = '\u001b[47m'
end = '\u001b[0m'
print(f'{white}{" " * 60}{end}')
print(f'{white}{" " * 12}{black}{" " * 11}{white}{" " * 14}{black}{" " * 11}{white}{" " * 12}{end}')
for i in range(3):
    print(
        f'{white}{" " * (10 - 2 * i)}{black}{" " * (i * 2 + 8)}{black}{" " * (7 + 2 * i)}{white}{" " * (10 - i * 4)}{black}{" " * (15 + 4 * i)}{white}{" " * (10 - 2 * i)}{end}')
for i in range(2):
    print(f'{white}{" " * 5}{black}{" " * 50}{white}{" " * 5}{end}')
for i in range(3):
    print(
        f'{white}{" " * (6 + i * 2)}{black}{" " * (16 - i * 2)}{black}{" " * (7 - i * 2)}{white}{" " * (2 + i * 4)}{black}{" " * (23 - i * 4)}{white}{" " * (6 + i * 2)}{end}')
print(f'{white}{" " * 12}{black}{" " * 11}{white}{" " * 14}{black}{" " * 11}{white}{" " * 12}{end}')
print(f'{white}{" " * 60}{end}')


print("Задание 3")
plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i / 2

step = round(abs(result[0] - result[9]) / 10, 2)
for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8 - i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k + 1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')

for i in range(10):
    pass


print("Задание 4")
file = open('sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))
file.close()
countneg = 0  # количество от -10 до -5
countpos = 0  # количество от 5 до 10
countall = 0
for k in range(len(list)):
    if -10 <= list[k] <= -5 or 5 <= list[k] <= 10:
        countall += 1
for i in range(len(list)):
    if -10 <= list[i] <= -5:
        countneg += 1
    elif 5 <= list[i] <= 10:
        countpos += 1
print(f'{white}{" " * (int(countneg/countall * 100))}{end}', round(countneg/countall * 100, 2), "%")
print(f'{white}{" " * (int(countpos/countall * 100))}{end}', round(countpos/countall * 100, 2), "%")
