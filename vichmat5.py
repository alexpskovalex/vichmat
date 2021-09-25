import math as m
accuracity=3
interval=20
a=0.2
b=8
eps=10**(-accuracity-1)

def sobaka(x):
    return x**(0.3)*(m.log(1.1*x)+x)

def simpson(b,e):
    n=1
    h=(b-0.1)/n
    x=[0.1+0*h,0.1+n*h]
    S1=h/3*(sobaka(x[0])+sobaka(x[1]))
    #S1=vspomogatsimpson(a,e)
    while True:
        n*=2
        h=(b-0.1)/n
        S2=S1
        S1=0
        for i in range(1,n):
            if i % 2 != 0:#нужно вставлять каждое нечетное значение
                x.insert(i,0.1+i*h)
            S1+=(3-(-1)**i)*sobaka(x[i])
        S1+=sobaka(x[0])
        S1+=sobaka(x[n])
        S1*=h/3
        if abs(S1-S2)<e:
            break
    return S2


def poisk_bebrenka(c,d):
    e=0.2
    while True:
        x=(c+d)/2

        if simpson(x,e)*simpson(c,e)<0:
            d=x
        else:
            c=x
        e/=2
        print('x:{0:9.{1}f}, f(x):{2:7.{1}f}'.format(x,accuracity,simpson(x,e)))
        # print (simpson(x,e))
        if  d-c<eps:
            break
    

poisk_bebrenka(a,b)