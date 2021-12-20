import math

e = 3
interval = 20
xmax = 5
xmin = 1

eps = 10**(-e)
interval_value = (xmax - xmin) / interval

def bebra(x):
    a = (math.sin(x))**2
    # print('a={0}, xuy ={1}, x={2}'.format(a,math.sin(x),x))
    b = math.log(a)
    return b + 0.2 * x

def poisk_bebrenka(c, d):
    count = 0
    while True:
        x = (c + d) / 2
        if bebra(x) * bebra(c) < 0:
            d = x
        else:
            c = x
        count += 1
        if not d - c > eps:
            break
    print('x:{0:9.{1}f}+-10^-7, f(x):{2:9.{1}f}, итераций:{3}'.format(x, e, bebra(x), count))

for i in range(1, interval + 1):
    a = xmin + interval_value * (i - 1)
    b = xmin + interval_value * (i)
    # print('{2}::a={0},b={1}'.format(a,b,i))
    if bebra(a) * bebra(b) <= 0:
        poisk_bebrenka(a, b)
# print(eps)