# 18. Реализовать алгоритм перемешивания списка. 

# первое решение
# import random

# list = [1,2,3,4,5,6]
# random.shuffle(list)
 
# print(list)


# второе решение
import random 
first_list = list(range(9))
for i in range(0,len(first_list)-1):
    j = random.randint(0,len(first_list)-1)
    first_list[i], first_list[j] = first_list[j], first_list[i]

print (first_list)