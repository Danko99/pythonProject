# 10. Фиксированная сумма

import itertools

pair = []


def recur_find(n):
    tmp = []
    if sum(list(pair[n])) == s:
        tmp = list(pair[n])
        tmp.reverse()
        return tmp
    elif n == 0:
        return -1
    else:
        return recur_find(n - 1)


s, l1, r1, l2, r2 = map(int, input().split())

if l1 > r1 or l2 > r2:
    print('Неправильные начальные условия')

x1 = list(range(l1, r1 + 1, 1))
x2 = list(range(l2, r2 + 1, 1))
pair = list(itertools.product(x1, x2))
print(recur_find(len(pair) - 1))
