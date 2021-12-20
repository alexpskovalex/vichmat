import math as m

accuracity = 7
e = 10**(-accuracity)
# a = 0
# b = m.pi
a=1
b=2.7
n = 1


def sobaka(x):
    # return m.exp(x) * m.cos(x)**2
    return (x*m.log(x))**2

def simpson(n, h):
    S = 0
    for i in range(1, n):
        if i % 2 != 0:  #нужно вставлять каждое нечетное значение
            x.insert(i, a + i * h)
        S += (3 - (-1)**i) * sobaka(x[i])
    S += sobaka(x[0])
    S += sobaka(x[n])
    S *= h / 3
    return S


h = (b - a) / n
x = [a + 0 * h, a + n * h]
count = 0
S1 = simpson(n, h)
while True:
    n *= 2
    h = (b - a) / n
    S2 = S1
    S1 = simpson(n, h)
    count += 1
    if abs(S1 - S2) < e:
        break
print('значение интеграла: {0:5.{1}f}, итераций: {2}, разбиений:{3}'.format(
    S2, accuracity, count, n))
