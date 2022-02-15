# 21. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#     список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
st = 'qwe'

count = 0

for i in range(len(list)): # чтобы i принимала значение индексов
    if list[i] == st:
        count += 1
        if count == 2:
            print(i)
            break
if count < 2:
    print(-1)