a = [[1.5, 3.9, 0.8, 9], [2.3, -3, 4.1, -8.2], [-2, 5, -0.9, 7.6], [1.8, 0.2, 6.2, -3]]
b = [-0.3, 1.5, 9, 0.1]
n = 4
x=[0,0,0,0]
for s in range(0,n-1):# 1-8
     for j in range(s,n):#2
          a[s][j]/=a[s][s]#2
     b[s]/=a[s][s]#3
     for i in range(s+1,n):#4-7
          for j in range(s,n):#5
               a[i][j]-=a[i][s]*a[s][j]#5
          b[i]-=b[s]*a[i][s]#6
x[n-1]=b[n-1]/a[n-1][n-1]#9
# print(s,' ',n-2)
for s in range(n-2,-1,-1):#10-12
     # print(s)
     x[s]=b[s]
     # print('s={0}'.format(s))
     for k in range(s+1,n):
          x[s]-=a[s][k]*x[k]
          # print('a[{1}][{2}] = {0:7.2f}'.format(a[s][k],s+1,k+1))
for m in range(0,4):
          print('{0:5.2f} {1:5.2f} {2:5.2f} {3:5.2f} | {4:5.2f}'.format(a[m][0],a[m][1],a[m][2],a[m][3],b[m]))
print('-----------')
for m in range(0,4):
     print('x[{0}] = {1:7.2f}'.format(m,x[m]))