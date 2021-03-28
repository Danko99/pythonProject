#5. Падение объекта
g=9.8
print('Введите значения для x,v,t')
x = float(input())
v = float(input())
t = float(input())
x_t=x+v*t - (g*pow(t,2))/2
print('x(t)=',x_t)
