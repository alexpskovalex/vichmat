import math

x = [0]
y = [1]
diff = []
dx = 0.02
h = dx
xmax = 0.5

def f(x, y):
    return (math.exp(x) * x - y) / 2

diff.append(f(x[0], y[0]))

def Runge_Kutta(i):
    k1 = h * f(x[i - 1], y[i - 1])
    k2 = h * f(x[i - 1] + h / 2, y[i - 1] + k1 / 2)
    k3 = h * f(x[i - 1] + h / 2, y[i - 1] + k2 / 2)
    k4 = h * f(x[i - 1] + h, y[i - 1] + k3)
    return y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

for i in range(3):  # заполняю 2 и 3 первых значения x, y и f(x,y)
    new_var = Runge_Kutta(len(y))
    y.append(new_var)
    x.append(x[-1] + dx)
    diff.append(f(x[-1], y[-1]))

while x[-1] < xmax:
    x.append(x[-1] + dx)
    subres_y = y[-1] + h / 24 * (55 * diff[-1] - 59 * diff[-2] + 37 * diff[-3] - 9 * diff[-4])
    y.append(subres_y)

for i in range(0, len(x)):
    print(" {0:4.2f} | {1:9.3f}".format(x[i], y[i]))