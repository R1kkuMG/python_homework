# 2.  Найти максимальное из пяти чисел

print ('Введите 1 число:')
a = int(input())
print ('Введите 2 число:')
b = int(input())
print ('Введите 3 число:')
c = int(input())
print ('Введите 4 число:')
d = int(input())
print ('Введите 5 число:')
e = int(input())

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