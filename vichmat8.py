xg = [3.2, 4.3, 5, 6.7, 7.5, 8.2, 9.1, 10]
yg = [4.4, 2.5, -0.7, -6.8, -7.6, -3.3, 6.5, 8.5]
xmin = 4
xmax = 9
dx = 0.5
ng = 8

def L(x):
    sum = 0
    for i in range(ng):
        product = 1
        for j in range(ng):
            if i != j:
                product *= (x - xg[j]) / (xg[i] - xg[j])
        sum += product * yg[i]
    return sum

x = xmin
while x <= xmax:
    print("x={0} f(x) = {1:7.5f}".format(x, L(x)))
    x += dx
