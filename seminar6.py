# # Из списка получить все элементы, которые больше 3

# my_list = [1, 2, 1, 4, 5]
# new_list = list(filter(lambda x: x > 3, my_list))
# print(new_list)


# # Из списка чисел получить квадраты этих чисел

# my_list = [1, 2, 1, 4, 5]
# new_list = list(map(lambda x: x**2, my_list))
# print(new_list)


# 1. Найти сумму квадратов чётных чисел на промежутке от 1 до n.
# Пример: n=5: [1, 2, 3, 4 ,5] --> 2^2 + 4^2 = 20

# n = int(input('n = '))
# res = list(filter(lambda x: not x%2, [i for i in range(1, n + 1)]))
# print(sum(list(map(lambda x: x**2, res))))


# 2. Из списка строк получить список, содержащий только те элементы, которые являются целыми числами
# Пример: lst = ['asd', '123', '1.23', 'ht', 'fwef322f'] --> ['123', '1.23']

# lst = ['asd', '123', '1.23', 'ht', 'fwef322f']
# my_list = list((filter(lambda x: x.isdigit(), lst)))
# print(my_list)


# 3. Посчитайте, сколько раз символ 'f' встречается в строке 'fmkasdo08f1fnacaofonfaf'.

# str1 = 'fmkasdo08f1fnacaofonfaf'
# print(str1.count('f'))

# str1 = 'fmkasdo08f1fnacaofonfaf'
# my_list = []
# res = list(filter(lambda x: my_list.append(x) if x == 'f' else False, str1))
# print(len(my_list))


# 4. Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков ( в данном случае ответ: [1, 2, 3, 5, 8, 13] ).

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# new_list = set(filter(lambda x: x in b, a))
# print(new_list)


# 5. Напишите программу, которая выводит чётные числа из заданного списка ( список чисел можно задачать любой самостоятельно ) и останавливается, если встречает число 237.

# a = [8, 1, 2, 3, 5, 8, 13, 21, 6, 3, 2, 34, 237, 55, 66, 12, 89, 14]
# num_index = [i for i in range(len(a)) if a[i] == 237]
# if num_index != []:
#     a = a[:num_index[0]]
# print([x for x in a if not x%2])
