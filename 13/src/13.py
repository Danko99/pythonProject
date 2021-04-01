#13. Простое число
import math
a = int(input())
i = 2
while i <= math.sqrt(a):
    i += 1
    if a % i == 0:
        print('Число составное')
        exit()
print('Число простое')
