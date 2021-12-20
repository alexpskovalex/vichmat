import math as m

a = [[1.5, 3.9, 0.8, 9], [2.3, -3, 4.1, -8.2], [4.4, 5, -0.9, 7.6], [1.8, 0.2, 6.2, -3]]
atest=a
b = [-0.3, 1.5, 9, 0.1]
btest = b
n = 4
accuracity = 5
eps = 10**(-accuracity)
x = []
counter = 0

def solve(x, counter):
    y = [0, 0, 0, 0]
    delta = [0, 0, 0, 0]
    for i in range(0, n):
        y[i] += b[i]
        for j in range(0, n):
            y[i] += a[i][j] * x[j]
        delta[i] = abs(x[i] - y[i])
    print('{0}:'.format(counter))
    print('иксы:  {0:12.7f} {1:12.7f} {2:12.7f} {3:12.7f}'.format(x[0], x[1], x[2], x[3]))
    print('игреки {0:12.7f} {1:12.7f} {2:12.7f} {3:12.7f}'.format(y[0], y[1], y[2], y[3]))
    print('дельты {0:12.8f} {1:12.8f} {2:12.8f} {3:12.8f}'.format(delta[0], delta[1], delta[2], delta[3]))
    if (max(delta) < eps) or (counter == 100):
        print('---------')
        print('ответ {0:8.5f} {1:8.5f} {2:8.5f} {3:8.5f}'.format(y[0], y[1], y[2], y[3]))
        return
    else:
        counter += 1
        for i in range(0, n):
            x[i] = y[i]
        solve(x, counter)

def schodimost():
    skhodimost = 0
    for i in range(0, n):
        for j in range(0, n):
            skhodimost += a[i][j]**2
    skhodimost = skhodimost**(1 / 2)
    if skhodimost > 1:
        print('a={0:5.3f}, условие сходимости не соблюдено'.format(skhodimost))
        return False
    else:
        return True


def printMatrix(msg):
    print(msg + ':')
    for m in range(0, n):
        print('{0:5.2f} {1:5.2f} {2:5.2f} {3:5.2f} | {4:5.2f}'.format(a[m][0], a[m][1], a[m][2], a[m][3], b[m]))
    print('-----------')

printMatrix('дано')
for i in range(0, n):
    for j in range(0, n):
        if i != j:
            a[i][j] /= -a[i][i]
            # print(a[i][i])
    b[i] /= a[i][i]
    a[i][i] = 0
printMatrix('после преобразований')
if schodimost():
    for i in range(0, n):
        x.append(-1000)

    solve(x, counter)
