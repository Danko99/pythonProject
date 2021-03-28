#4. Обмен значениями
print('Введите два целых числа')
a = int(input())
b = int(input())
tmp=a
a=b
b=tmp
print('a=',a, ',b=', b)
a, b = b, a
print('a=',a, ',b=', b)
