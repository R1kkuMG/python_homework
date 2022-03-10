# 22. Найти сумму чисел списка стоящих на нечетной позиции

#первое решение
# list = [1,3,5,7,9,11]
# summ = 0
# for i in range(len(list)): # чтобы i принимала значение индексов
#     if i % 2 != 0:
#         # print (list[i])
#         summ = summ + list[i]
# print(summ)


#второе решение
# mylist = list(range(5))
# print(mylist)

# print(sum(mylist[1::2]))

n = int(input('n = '))
print(sum(list(filter(lambda x: x%2, [x for x in range(1, n + 1)]))))