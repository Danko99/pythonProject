#6. Корни уравнения
import math
print("Введите коэффициенты для уравнения")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discrim= pow(b,2) - 4 * a * c
print(f'Дискриминант D = {discrim}')
if discrim > 0:
    x1 = (-b + math.sqrt(discrim)) / (2 * a)
    x2 = (-b - math.sqrt(discrim)) / (2 * a)
    print('x1=',x1,'x2=',x2)
elif discrim == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    print("Корней нет")