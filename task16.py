# 16. Задать список из n чисел последовательности (1+(1/n))^n и вывести на экран их сумму

print(sum(list(map(lambda n: (1 + (1/n)) ** n, [n for n in range(1, 10)]))))