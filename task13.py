# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# find - вернет индекс самого первого совпадения

st1 = 'qwertyqwqw'
st2 = 'qw'

flag = True
count = 0

while flag:
    now_index = st1.find(st2)
    if now_index != -1:
        st1 = st1[now_index + len(st2):]
        count += 1
    else:
        print(count)
        flag = False