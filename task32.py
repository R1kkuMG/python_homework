# 32. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#     Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []

# def f_1(x):
#     global new_list
#     if x not in new_list:
#         new_list.append(x)

# f = lambda x: new_list.append(x) if x not in new_list else False

res = list(filter(lambda x: new_list.append(x) if x not in new_list else False, my_list))
print(new_list)