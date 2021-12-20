import math
import random as r

e = 3
eps = 0.1**e

g = 10**(-3)
x = 1.5
y = 1.3
a = 0.02
h = 0.08

def funct(x, y):
    a = math.sin((x - 0.73)**2 + 0.33 * y**2)
    b = math.cos(0.51 * (x - 0.79)**2 + 1.35 * (y - 1.38)**2)
    c = 0.78 * x**2 + 0.91 * y**2
    return a + b + c
print("   x   |   y   |  df/dx  |  df/dy |  grad  | f(x,y)|counter")
diffx = (funct(x + g, y) - funct(x - g, y)) / 2 / g
diffy = (funct(x, y + g) - funct(x, y - g)) / 2 / g
x -= h * diffx
y -= h * diffy
xold1 = x
yold1 = y

diffx = (funct(x + g, y) - funct(x - g, y)) / 2 / g
diffy = (funct(x, y + g) - funct(x, y - g)) / 2 / g
x -= h * diffx
y -= h * diffy
count = 0
while True:

    xold2 = xold1
    yold2 = yold1
    xold1 = x
    yold1 = y
    count += 1
    diffx = (funct(x + g, y) - funct(x - g, y)) / 2 / g
    diffy = (funct(x, y + g) - funct(x, y - g)) / 2 / g
    absgrad = (diffx**2 + diffy**2)**(1 / 2)
    if (absgrad < eps) or (count > 100):
        break

    else:
        x -= a * (xold1 - xold2) + h * diffx
        y -= a * (yold1 - yold2) + h * diffy

    print("{0:6.3f} | {1:6.3f} | {2:6.3f} | {3:6.3f} | {4:6.3f} | {5:6.3f}| {6:3} ".format(x, y, diffx, diffy, absgrad, funct(x, y), count))