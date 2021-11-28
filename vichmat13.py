import math 
import random as r
#   x   |  y    | df/dx | df/dy | grad | f(x,y)
# 0.304 | 0.104 | 0.000 | 0.001 | 0.001 | -0.414

  #попытка попасть №1
e = 3
eps = 0.1**e
# g = 10**(-2)*14
# a = 0.005
# h = 0.07
g = 10**(-3)
while True:
    x = 1.5
    y = 1.3
    
    h = 10**(-2)*r.randint(1,100)
    a = 10**(-2)*r.randint(1,100)
    zaebal=0
    def funct(x, y):
        a = math.sin((x - 0.73)**2 + 0.33 * y**2)
        b = math.cos(0.51 * (x - 0.79)**2 + 1.35 * (y - 1.38)**2)
        c = 0.78 * x**2 + 0.91 * y**2
        return a + b + c



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
    # xold1 = x
    # yold1 = y
    zaebal = 0
    # print("   x   |   y   |  df/dx  |  df/dy |  grad  | f(x,y)|counteeer")
    while True:

        xold2 = xold1
        yold2 = yold1
        xold1 = x
        yold1 = y
        zaebal += 1
        diffx = (funct(x + g, y) - funct(x - g, y)) / 2 / g
        diffy = (funct(x, y + g) - funct(x, y - g)) / 2 / g
        absgrad = (diffx**2 + diffy**2)**(1 / 2)
        # print("{0:6.3f} | {1:6.3f} | {2:6.3f} | {3:6.3f} | {4:6.3f} | {5:6.3f}| {6:3} ".format(x, y, diffx, diffy, absgrad, funct(x, y), zaebal))
        if (absgrad < eps) or (zaebal > 100):
            if zaebal<50:
                print("a= {0:4.2f}".format(a))
                print("h= {0:4.2f}".format(h))
                print("g= {0:4.2f}".format(g))
                print("-------------")
            break
            
        else:
            x -= a * (xold1 - xold2) + h * diffx
            y -= a * (yold1 - yold2) + h * diffy
            
    if zaebal<29:
        break
print("{0:6.3f} | {1:6.3f} | {2:6.3f} | {3:6.3f} | {4:6.3f} | {5:6.3f}| {6:3} ".format(x, y, diffx, diffy, absgrad, funct(x, y), zaebal))
print("a= {0:4.2f}".format(a))
print("h= {0:4.2f}".format(h))
print("g= {0:4.2f}".format(g))
print("0.402 | -0.110 |  0.001 | -0.000 |  0.001 | -0.749|  32")