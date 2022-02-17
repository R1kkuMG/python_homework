# 22. Найти сумму чисел списка стоящих на нечетной позиции

list = [1,3,5,7,9,11]
summ = 0
for i in range(len(list)): # чтобы i принимала значение индексов
    if i % 2 != 0:
        # print (list[i])
        summ = summ + list[i]
print(summ)