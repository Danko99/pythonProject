#8. Калькулятор
A = [str(i) for i in input().split()]
if len(A)>3:
    print('Количество значений больше 3')
    exit()

if A[1] == '+':
    print(int(A[0], 10) + int(A[2], 10))
elif A[1] == '-':
    print(int(A[0], 10) - int(A[2], 10))
elif A[1] == '*':
    print(int(A[0], 10) * int(A[2], 10))
elif A[1] == '/':
    print(int(A[0], 10) / int(A[2], 10))
else:
    print('Неверная операция')