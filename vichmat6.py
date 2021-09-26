a = [[1.5, 3.9, 0.8, 9], [ 2.3, -3, 4.1, -8.2], [4.4, 5, -0.9, 7.6], [1.8, 0.2, 6.2, -3]]
b = [ -0.3, 1.5, 9, 0.1]
n = 4
x = [0, 0, 0, 0]
print('дано:')
for m in range(0, n):
    print('{0:5.2f} {1:5.2f} {2:5.2f} {3:5.2f} | {4:5.2f}'.format(a[m][0], a[m][1], a[m][2], a[m][3], b[m]))
print('-----------')

for s in range(0,n):
     for i in range(s+1,n):
          k=a[i][s]/a[s][s]
          for j in range(s,n):
               a[i][j]-=k*a[s][j]
          b[i]-=k*b[s]
          
for i in range(0,n):
     b[i]/=a[i][i]
     for j in range(n-1,i-1,-1):
          a[i][j]/=a[i][i]

for s in range (n-1,-1,-1):
     x[s]=b[s]
     for k in range(n-1,s,-1):
          x[s]-=a[s][k]*x[k]
print('-после преобразований:')
for m in range(0, n):
    print('{0:5.2f} {1:5.2f} {2:5.2f} {3:5.2f} | {4:5.2f}'.format(a[m][0], a[m][1], a[m][2], a[m][3], b[m]))
print('-----------')
print('-ответы-')
for m in range(0, 4):
    print('x[{0}] = {1:7.2f}'.format(m, x[m]))
print('-----------')