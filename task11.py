# 11. Сформировать список из  N членов последовательности.
#     Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = 1
print (n)
for e in range(0, 5):
    n *= (-3)
    print(n)