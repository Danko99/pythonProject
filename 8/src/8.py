A = [0, 0, 0]

A[0], A[1], A[2] = map(str, input().split())

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