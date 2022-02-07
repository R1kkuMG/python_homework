# # первое решение задачи
# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
# с = int(input('Введите третье число:'))
# max = a
# if b > a:
#     max = b
# if с > b:
#     max = с
# print (f'максимальное число = {max}')

# # второе решение задачи
# listNums = [5,2,32]
# max = listNums[0]
# for i in range(1,len(listNums)):
#     if listNums[i] > max:
#         max = listNums[i] 
# print (f'{listNums}, {max}')

# # третье решение задачи
# listNums = [5,2,32]
# max = listNums[0]
# for i in listNums:
#     if i > max:
#         max = i 
# print (f'{listNums}, {max}')

#Задача на нечетность
a = int (input ('Введите число:'))
if a % 2 == 0:
    print (f'Число {a} является четным')
else:
    print (f'Число {a} является нечетным')