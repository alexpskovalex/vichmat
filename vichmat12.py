import math
#   x   |  y    | df/dx | df/dy | grad | f(x,y)
# 0.304 | 0.104 | 0.000 | 0.001 | 0.001 | -0.414
x = 1.5
y = 1.3
# h = 0.2  #попытка попасть №0
# h = 0.3  #попытка попасть №1
h = 0.1 #попытка попасть №1
e=3
eps=0.1**e
g=10**(-3)
def funct(x, y):
    a = math.sin((x - 0.73)**2 + 0.33 * y**2)
    b = math.cos(0.51 * (x - 0.79)**2 + 1.35 * (y - 1.38)**2)
    c = 0.78 * x**2 + 0.91 * y**2
    return a + b + c

zaebal=0 # НАСТЯ ЕСЛИ ЯЗАБУДУ УДАЛИ ЭТО
print("  x   |  y   | df/dx  | df/dy | grad  | f(x,y)")
while True:
    zaebal+=0
    diffx =(funct(x+g,y)-funct(x-g,y))/2/g
    diffy =(funct(x,y+g)-funct(x,y-g))/2/h
    absgrad=(diffx**2+diffy**2)**(1/2)
    print("{0:5.3f} | {1:5.3f} | {2:5.3f} | {3:5.3f} | {4:5.3f} | {5:5.3f} ".format(x,y,diffx,diffy,absgrad,funct(x,y)))
    if (absgrad<eps) or (zaebal>1000):
        break
    else:
        x-=h*g
        y-=h*g