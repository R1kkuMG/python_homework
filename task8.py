# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 

def plosk (x, y):
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            print('Первая четверть')
        if x < 0 and y > 0:
            print('Вторая четверть')
        if x < 0 and y < 0:
            print('Третья четверть')
        if x > 0 and y < 0:
            print('Четвертая четверть')
    else:
        print("Error")

x = float(input('Введите координату X: '))
y = float(input('Введите координату Y: '))
plosk (x, y)