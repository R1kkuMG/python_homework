# 3. Вывести на экран числа от -N до N

print ('Введите любое целое число:')
a = int(input())

res = -a
while res <= a:
    print (res)
    res += 1