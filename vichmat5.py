import math as m
e=3
accuracity=5
e=10**(-accuracity)
a=0
b=m.pi
n=1

def sobaka(x):
    return m.exp(x)*m.cos(x)**2

def simpson(n):
    S=0
    for i in range(1,n):
        if i % 2 != 0:#нужно вставлять каждое нечетное значение
            x.insert(i,a+i*h)
        S+=(3-(-1)**i)*sobaka(x[i])
    S+=sobaka(x[0])
    S+=sobaka(x[n])
    S*=h/3
    return S

h=(b-a)/n
x=[a+0*h,a+n*h]
count=0
