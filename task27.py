# 27. Строка содержит набор чисел. Показать большее и меньшее число

a = '13 2 455 10123 67 1123 876 23 54'
a = a.split()
b = []
for i in a:
    b.append(int(i))
print(b)

max = b[0]
for i in range(len(b)):
    if b[i] > max:
        max = b[i]

min = b[0]
for i in range(len(b)):
    if b[i] < min:
        min = b[i]

print (min)
print (max)

# ИЛИ
# print(f'Max is {max(b)}') - max Это функция, определяющая макс
# print(f'Min is {min(b)}') - min Это функция, определяющая мин