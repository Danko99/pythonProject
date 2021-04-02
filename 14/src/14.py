# 14. Степень двойки
import math

n = int(input())
count = 0
i = 0
while i < n:
    if math.pow(2, i) < n:
        count += 1
    i = i + 1
print(count)
