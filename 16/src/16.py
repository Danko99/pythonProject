# 16. Хобби
import re

n = int(input())
A = input().split()

if len(A) != n:
    print('Количество билетов не совпадает с указанными билетами')

regex = re.compile(r"(^a...55661)")
list_of_string = [s for s in A if regex.match(s)]

if len(list_of_string) != 0:
    print(list_of_string)
else:
    print(-1)
