import math as m


def f(x,y):
    # print(x)
    # print(y)
    # print((3.81*x**2)+(0.3*y**2))
    return 20*x+0.4*y+m.exp(3.81*x**2+0.3*y**2)

def fx(x,y):
    return 20+m.exp(3.81*x**2+0.3*y**2)*2*3.81*x

def fy(x,y):
    return 0.4+m.exp(3.81*x**2+0.3*y**2)*0.3*2*y

def grad(x,y):
    return (fx(x, y) ** 2 + fy(x, y) ** 2) ** 0.5
e = 1
eps = 0.1**e
x0 = -0.3
y0 = -0.3

x = 0
y = 0
a0 = 0.1
N=20
i=0
n=0
print("    x       y    f(x,y)  ak")
while (True):  
    gradient = grad(x0, y0)
    if (abs(gradient) <= eps):
        break

    i = 1
    fnew = f(x0, y0)
    while (True):
        xn = x0 - i * a0 * fx(x0, y0)
        yn = y0 - i * a0 * fy(x0, y0)
        F_old = fnew
        fnew = f(xn, yn)
        if (fnew > F_old):
            break
        i+=1
    
    
    if (n >= N):
        break

    ak = a0 * (i - 1)
    if (ak > 0):
        x0 = x0 - ak * fx(x0, y0)
        y0 = y0 - ak * fy(x0, y0)
        n+=1
        print(" {0:5.3f}  {1:5.3f} {2:5.3f} {3:5.3f} ".format(x0,y0,f(x0,y0),ak))
    else:
        a0 /= 10
    


