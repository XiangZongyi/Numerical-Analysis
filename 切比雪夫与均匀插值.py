import math
import numpy as np
import matplotlib.pyplot as plt

n = eval(input('输入n：'))

def fun(x):
    return  math.exp(np.abs(x))

def Newtdd(n):
    X1 = []
    Y1 = []
    d = 2/n
    x0 = -1
    for i in range(n+1):
        X1.append(x0)
        y = fun(x0)
        Y1.append(y)
        x0 = x0+d
    return X1,Y1

def funy(x,n,X,Y):
    C = np.zeros((n+1,n+1))
    for i in range(n+1):
        C[i, 0] = Y[i]
    for i in range(2, n + 2):
        for j in range(1, n+1 - i + 2):
            C[j - 1, i - 1] = (C[j, i - 2] - C[j - 1, i - 2]) / (X[j + i - 2] - X[j - 1])
    D = [] # 用于存放系数
    for i in range(1, n + 2):
        c = C[0, i - 1]
        D.append(c)
    c1 = D[1]
    x1 = x - X[0]
    p = D[0] + c1 * x1
    for i in range(1,n):
        x1 = x1*(x-X[i])
        c1 = D[i+1]
        p = p + x1 * c1
    return p

def Chebyshev(n):
    X2 = []
    Y2 = []
    for i in range(1,n+2):
        x = math.cos((2*i-1)*math.pi/(2*n))
        X2.append(x)
        y = fun(x)
        Y2.append(y)
    return X2,Y2

# 画图
plt.figure(figsize=(10,5))
plt.xlim(-1,1)

# 第一个图
plt.subplot(121)
plt.title('Union')
plt.xlabel('x')
plt.ylabel('y')
X1,Y1= Newtdd(n)
plt.scatter(X1,Y1,marker='o',color='red')
x = np.linspace(-1,1,200)
y = funy(x,n,X1,Y1)
plt.plot(x,y)

# 第二个图
plt.subplot(122)
plt.title('Chebyshev')
plt.xlabel('x')
plt.ylabel('y')
X2,Y2 = Chebyshev(n)
plt.scatter(X2,Y2,marker='o',color='red')
x = np.linspace(-1,1,200)
y = funy(x,n,X2,Y2)
plt.plot(x,y)
plt.show()









