import numpy as np
n = int(input("输入n:"))
D = np.zeros([n, n])
L = np.zeros([n, n])
U = np.zeros([n, n])

# 构造D矩阵
for i in range(n):
    D[i, i] = 3
# 构造L矩阵
for i in range(n-1):
    U[i, i+1] = -1
# 构造U矩阵
for i in range(n-1):
    L[i+1, i] = -1
A = D + U + L
b = np.ones([n, 1])
b[0, 0] = 2
b[n-1, 0] = 2

x_ = np.ones([n, 1])
x0 = np.zeros([n, 1])
index = np.linalg.norm(x_ - x0, ord=np.inf)

def gos(x0, index):
    num = 0
    D_inv = np.linalg.inv(D)
    x1 = x0
    while index > 1e-6:
        x1 = np.dot(D_inv, (b - np.dot(U, x0) - np.dot(L, x1)))
        x0 = x1
        num = num + 1
        index = np.linalg.norm(x_ - x0, np.inf)
    error = np.linalg.norm(b-np.dot(A, x1), np.inf)
    print("高斯方法计算结果：", x1)
    print("高斯方法计算步数：", num)
    print("高斯方法后向误差：", error)

def SOR(x0, index):
    w = 1.2
    inv = np.linalg.inv(w*L + D)
    num = 0
    while index > 1e-6:
        x1 = np.dot(inv, (1-w)*np.dot(D, x0) - w*np.dot(U, x0) + w*b)
        x0 = x1
        num = num+1
        index = np.linalg.norm(x_ - x0, np.inf)
    error = np.linalg.norm(b - np.dot(A, x1), np.inf)
    print("SOR计算结果：", x1)
    print("SOR计算步数：", num)
    print("SOR后向误差：", error)

SOR(x0 ,index)



