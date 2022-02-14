# value = None

# a = 123
# b = 1.23
# value = 12345
# # print(type(a)) 
# print(type(b)) 
# print(type(value)) 

# s = 'hello world'
# print(s) # вывод строки
    
# print (a, '-',b, '-',s)
# print ('{1} - {2} - {0}'.format(a, b, s))
# print (f'{a} - {b} - {s}')

# f = True
# print (f)

# СПИСКИ
# list = ['1', '2', '3', 'hello world']
# print (list)

# ВВОДВЫВОД ДАННЫХ
# print ('Введите a')
# a = int(input())
# print ('Введите b')
# b = int(input())
# print (a, ' + ', b, ' = ', a+b)
# # print (f'{a} {b}')

# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ
# a = 1.3
# b = 3
# c = round(a*b,3)
# print (c)

# СОКРАЩЕННЫЕ ОПЕРАЦИИ
# a = 3
# a += 5
# print (a)

# ЛОГИЧЕСКИЕ ОПЕРАЦИИ
# a = 1 != 2
# a = 'qwe'
# b = 'qwe'
# a = 1 < 3 < 5

# func = 1
# T = 4
# x = 123

# f = 2 < 3 or 4 > 6

# f = [1, 2, 3, 4]
# # print (not 2 in f)

# is_odd = f[0] % 2 == 0
# print (is_odd)

# orig = 23
# inv = 0

# while orig != 0:
#     inv = inv * 10 + (orig % 10)
#     orig //= 10
# else:
#     print ('Пожалуй')
#     print ('хватит ) ')
# print (inv)

# r = range(10)
# # for i in range(1,10,2):
# for i in 'qwerty':
#     print (i)

# ФУНКЦИИ
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 2
# print (f(arg))
# print (type(f(arg)))

# РАБОТА С ФАЙЛАМИ

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # r - для чтения, w - для записи
# # data.writelines(colors) # разделителей не будет
# data.write ('\nLINE 2\n')
# data.write ('LINE 3\n')
# data.close() # нужно для того, чтобы не было утечек памяти

# with open('file.txt', 'a') as data:
#     data.write ('LINE 1111\n')
#     data.write ('LINE 22222\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# ФУНКЦИИ

# import hello as h
# print (h.f(1))


# def new_string(symbol, count = 3): # можно заранее задачть значение аргументов
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12


# def concatenatio(*params): # * - указывает на передачу неограниченного кол-ва элементов
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ... нельзя передать числа, так как это строка


# РЕКУРСИЯ

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


# КОРТЕЖ

# t = () 
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')


# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support item assignment


# t = tuple(['red', 'green', 'blue']) # двойное преобразование: список -> кортеж, котртеж -> независимые переменные
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue


# СЛОВАРИ

# dictionary = {} # создание пустого словаря
# dictionary = \
#     {
#         'up': '↑', # ключ и значение
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'} посмотреть на весь словарь  
# print(dictionary['left']) # ← посмотреть конкретное значение через ключ
# # типы ключей могут отличаться
# for k in dictionary.keys(): # печатает ключи
#     print(k)
# for k in dictionary.values(): # печатает значения
#     print(k)
# for v in dictionary: # печатает ключи
#     print(v)
# for v in dictionary: # печатает значения
#     print(dictionary[v])


# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# down: ↓
# right: →



# МНОЖЕСТВА

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set


# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}


# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') # элементы можно добавлять
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # элементы можно удалять
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } очистить множества
# print(colors) # set()


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} копируем одно множество в другое
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединяем два множества (b - аргумент)
# i = a.intersection(b) # i = {8, 2, 5} пересечение множеств
# dl = a.difference(b) # dl = {1, 3} разница множеств
# dr = b.difference(a) # dr = {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}


# a = {1, 2, 3, 5, 8}
# b = frozenset(a) # сделать множестов неизменяемым
# print(b) # frozenset({1, 2, 3, 5, 8})



# СПИСКИ

# list1 = [1,2,3,4,5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123
# list2[1] = 333

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)


list1 = [1,2,3,4,5]
# print(list1.pop()) # удаление последнего элемента из списка
# print(len(list1))
# print(list1)

# print(list1.pop(2)) # удаление 2ого элемента из списка
# print(list1)

# print(list1.insert(2, 11)) # добавление 2ого элемента (сначала позиция, потом значение)
# print(list1)

print(list1.append(11)) # добавление элемента в конец списка
print(list1)