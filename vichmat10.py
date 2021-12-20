import math

y = [1]
x = [0]
dx = 0.02
h = dx
xmax = 0.5

def f(x, y):
    return (math.exp(x) * x - y) / 2 # y'= выражаем производную

n = x[0]
while x[-1] < xmax:
    x.append(x[-1] + dx)
    yhelp = y[-1] + h / 2 * f(x[-1], y[-1])
    y.append(y[-1] + h * f(x[-1]+h/2, yhelp))
for i in range(0, len(x)):
    print(" {0:4.2f} | {1:9.3f}".format(x[i], y[i]))
# print(f(3,9))