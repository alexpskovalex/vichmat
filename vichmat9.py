xg = [1.1, 1.3, 1.6, 2.1, 2.2, 2.6, 2.9, 3]
yg = [2.1, 2.8, -4.4, 3.6, -8.7, 7.2, 7.6, 3.4]
n = len(xg)
m = 4
a = []
b = []
for i in range(m + 1):
    a.append([])
    for j in range(m + 1):
        sum = 0
        for k in range(n):
            sum += xg[k]**((i + 1) + (j + 1)-2)
        a[i].append(sum)
for i in range(m + 1):
    sum = 0
    for k in range(n):
        sum += yg[k] * xg[k]**(i)
    b.append(sum)

def printMatrix(msg):
    print(msg + ':')
    for ra in range(len(b)):
        print('{0:8.2f} {1:8.2f} {2:8.2f} {3:8.2f} {4:8.2f} | {5:8.2f} '.format(a[ra][0], a[ra][1], a[ra][2], a[ra][3], a[ra][4], b[ra]))
    print('-----------')

def gaus(a, b):
    n = len(b)
    x = [0,0,0,0,0]
    for s in range(0, n):
        for i in range(s + 1, n):
            k = a[i][s] / a[s][s]
            for j in range(s, n):
                a[i][j] -= k * a[s][j]
            b[i] -= k * b[s]

    for i in range(0, n):
        b[i] /= a[i][i]
        for j in range(n - 1, i - 1, -1):
            a[i][j] /= a[i][i]

    for s in range(n - 1, -1, -1):
        x[s] = b[s]
        for k in range(n - 1, s, -1):
            x[s] -= a[s][k] * x[k]
    printMatrix("после преобразований:")
    return x

def P(a, x):
    p = []
    for i in range(n):
        sum = 0
        for j in range(m + 1):
            sum += a[j] * x[i]**(j)
        p.append(sum)
    return p

printMatrix("test")
alpha = gaus(a, b)
p = P(alpha, xg)
sumn=0
for i in range(n):
    print('x= {1:3.2f} дано {0:3.2f} получилось {2:3.2f} невязка {3:3.2f} '.format(yg[i],xg[i],p[i],p[i]-yg[i]  ) )
    sumn+=(p[i]-yg[i])**2 
print('итого нвязка {0:5.3f}'.format(sumn))