#11. Возведение в степень
x = int(input("Число = "))
y = int(input("Степень = "))

i = 1
while i < y:
    i += 1
    x *= x

print(x)
