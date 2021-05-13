#28. Факторизация натурального числа
from collections import Counter
n = int(input("Integer: "))
factors = []
d = 2
m = n
while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n//=d
        else:
            d += 1
factors.append(n)
f_factors = Counter(factors)

str = str(f_factors)
str = str.replace("Counter({", "")
str = str.replace("})", "")
str = str.replace(": 1", "", len(f_factors))
str = str.replace(", ", "*", len(f_factors))
str = str.replace(": ", "^", len(f_factors))
print(str)


