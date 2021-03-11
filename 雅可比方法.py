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
D_inv = np.linalg.inv(D)

# x_ 位正确解
x_ = np.ones([n, 1])
x0 = np.zeros([n, 1])
index = np.linalg.norm(x_ - x0, ord=np.inf)

num = 0
# 计数
while index >= 1e-6:
    x1 = np.dot(D_inv,(b-np.dot((L+U),x0))) # 注意用矩阵乘法np.dot
    index = np.linalg.norm(x_ - x1, ord=np.inf)
    x0 = x1
    num = num + 1

error = np.linalg.norm(b-np.dot(A, x1), ord=np.inf)
print("计算结果:", x1)
print("计算步数：", num)
print("后向误差：", error)


