# 14. Подсчитать сумму цифр в вещественном числе.

num = float(input('Введите дробное число: '))
summ = 0
for i in str(num):
    if i != '.':
        summ += int(i)
print(f' Сумма = {summ}')