# 2.  Найти максимальное из пяти чисел

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))
d = int(input('Введите 4 число: '))
e = int(input('Введите 5 число: '))

max = a
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
if e > max:
    max = e
print (f'Максимальное число = {max}')