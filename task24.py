# 24. В заданном списке вещественных чисел найдите разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# trunc - откидывает дробную часть

from math import *
a = [1.1, 1.2, 3.1, 5, 10.01]

for i in range(len(a)):
    a[i] = a[i] - trunc(a[i]) 

print(max(a) - min(a))