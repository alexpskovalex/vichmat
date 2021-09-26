import math as m

e = 7
a = 0
b = m.pi
n = 60

h = (b - a) / n
delta = h / 2
x0 = a + 0 * h
xn = a + n * h

def sobaka(x):
    return m.exp(x) * m.cos(x)**2

def pryamougolnik():
    S = 0
    for i in range(0, n):  #range невключительно конец
        x = a + i * h
        S += sobaka(x + delta)
    S *= h
    print('метод прямоугольников:S = {0:5.{1}f}'.format(S, e))

def trapeciya():
    S = 0
    for i in range(1, n):
        x = a + i * h
        S += sobaka(x)
    S *= 2
    S += sobaka(x0)
    S += sobaka(xn)
    S *= h / 2
    print('метод трапеций:S = {0:5.{1}f}'.format(S, e))

def simpson():
    S = 0
    # for i in range(1,n-1):
    #     x=a+i*h
    #     S+=4*sobaka(x)
    # for i in range(2,n-2):
    #     x=a+i*h
    #     S+=2*sobaka(x)
    for i in range(1, n):
        x = a + i * h
        S += (3 - (-1)**i) * sobaka(x)
    S += sobaka(x0)
    S += sobaka(xn)
    S *= h / 3
    print('метод Симпсона:S = {0:5.{1}f}'.format(S, e))

pryamougolnik()
trapeciya()
simpson()