# 16. Задать список из n чисел последовательности (1+(1/n))^n и вывести на экран их сумму


summ = 0
for n in range(1, 6):
    x = (1 + (1/n)) ** n
    print(x)
    summ = summ + x
print(summ)