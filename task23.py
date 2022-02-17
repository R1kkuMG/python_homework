# 23. Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

list = [2,3,4,5,6,7]
list2 = []
mult = 0
print(list)
for i in range(len(list)):
    mult = list[i]*list[len(list) - 1 - i]
    if i < len(list)/2:
        list2.append(mult)    
print(list2)