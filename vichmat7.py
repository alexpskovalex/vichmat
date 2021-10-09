a = ((1.5, 3.9, 0.8, 9), (2.3, -3, 4.1, -8.2), (4.4, 5, -0.9, 7.6), (1.8, 0.2, 6.2, -3))
u2 = [1, 0, 0, 0]
n = 4
e = 3
count = 0
lmb2 = -1

def mat_mult(a, b):
    res = [0, 0, 0, 0]
    for i in range(n):
        subsum = 0
        for j in range(n):
            subsum += a[i][j] * b[j]
        res[i] = subsum
    return res

def vec_length(a):
    sum = 0
    for i in range(n):
        sum += a[i]**2
    sum = sum**(1 / 2)
    return sum

while True:
    count += 1
    u1 = u2
    u2 = mat_mult(a, u1)
    lmb1 = lmb2
    lmb2 = vec_length(u2) / vec_length(u1)
    # print("итерация {0}: lmb ={2} {1} ".format(count,u2,lmb2))
    if abs(lmb1 - lmb2) < 10**(-e):
        break
print("итерация {0}: приблеженное значение lmb = {1} приблеженное значение собственного вектора {2}  ".format(count, lmb2, u2))
