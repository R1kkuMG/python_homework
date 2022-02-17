# 26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
#     Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# рекурсия для отрицательных
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n - 2) - fib(n - 1)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)

# рекурсия для положительных
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34