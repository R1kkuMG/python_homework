# 1. Сформировать список из N членов последовательности. Список записать в файл
# "number_list.txt" (в одну строку - одно число).

# n = 5
# with open('number_list.txt', 'w') as data:
#    for e in range(0, 10):
#         data.write(f'{n * -3}\n')
#         n *= (-3)


# 2. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой

# find - вернет индекс самого первого совпадения

# st1 = 'qwertyqwqw'
# st2 = 'qw'

# flag = True
# count = 0

# while flag:
#     now_index = st1.find(st2)
#     if now_index != -1:
#         st1 = st1[now_index + len(st2):]
#         count += 1
#     else:
#         print(count)
#         flag = False

# 3. Подсчитать сумму цифр в вещественном числе.

# num = float(input('Введите дробное число: '))
# summ = 0
# for i in str(num):
#     if i != '.':
#         summ += int(i)
# print(f' Сумма = {summ}')

# 4. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    # Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# num = int(input('Введите число: '))
# dictionary = {}
# for i in range(1, num+1):
#     dictionary[i - 1] = 3 * i + 1
# print(dictionary)


# 5. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#   Cписок: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

# list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# st = 'qwe'

# count = 0

# for i in range(len(list)): # чтобы i принимала значение индексов
#     if list[i] == st:
#         count += 1
#     if count == 2:
#         print(i)
#         break