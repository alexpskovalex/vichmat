import math as m

accuracity = 7
a = 0.2
b = 8
eps = 10**(-accuracity)

def sobaka(x):
    return x**(0.3) * (m.log(1.1 * x) + x)
    # return (m.log(0.1 * x) + m.exp(0.4 * x)) / (m.sin(x) + 1.5)

def simpson(b, e):
    n = 1
    h = (b - 0.1) / n
    x = [0.1 + 0 * h, 0.1 + n * h]
    S1 = h / 3 * (sobaka(x[0]) + sobaka(x[1]))
    #S1=vspomogatsimpson(a,e)
    while True:
        n *= 2
        h = (b - 0.1) / n
        S2 = S1
        S1 = 0
        for i in range(1, n):
            if i % 2 != 0:  #нужно вставлять каждое нечетное значение
                x.insert(i, 0.1 + i * h)
            S1 += (3 - (-1)**i) * sobaka(x[i])
        S1 += sobaka(x[0])
        S1 += sobaka(x[n])
        S1 *= h / 3
        if abs(S1 - S2) < e:
            break
    return S2

def poisk_bebrenka(c, d):
    e = 0.2
    count = 0
    print(' # |     x     |    f(x)  ')
    while True:
        x = (c + d) / 2
        if simpson(x, e) * simpson(c, e) < 0:
            d = x
        else:
            c = x
        e /= 2
        count += 1
        print('{3:2} | {0:5.{1}f} | {2:7.{1}f}'.format(x, accuracity, simpson(x, e), count))
        # print (simpson(x,e))
        if d - c < eps:
            break
    print('------------------')
    print('ответ: x={0:5.{1}f}+-{4}, f(x)={2:7.{1}f}, итераций:{3}'.format(x, accuracity, simpson(x, e), count, eps))

poisk_bebrenka(a, b)
