# 7. Площадь треугольника
import math

print("Выберите способ расчета площади")
a = float(input("Способ = "))

if a == 1:
    print("Способ расчета площади через длины сторон  a,b,c")
    print("Введите длины сторон a,b,c")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('S =', s)

elif a == 2:
    print("Способ расчета площади через координаты вершин A,B,C")
    print("Введите координаты вершин A,B,C")
    A = [0, 0]
    B = [0, 0]
    C = [0, 0]
    A[0], A[1] = map(int, input().split())
    B[0], B[1] = map(int, input().split())
    C[0], C[1] = map(int, input().split())
    s = math.fabs((A[1] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1])) / 2
    print('S =', s)

else:
    print("Недопустимый ввод")
