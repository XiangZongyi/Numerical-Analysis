import numpy as np

n = eval(input("输入的点个数："))
X = []
Y = []
for i in range(n):
    x, y = eval(input("分别输入坐标x与y(用逗号分隔):"))
    X.append(x)
    Y.append(y)
# 矩阵 C 用于存储多项式系数
C = np.zeros((n, n))
for i in range(n):
    # 矩阵第一列存放Y中元素
    C[i, 0] = Y[i]

# 第i列,构建三角形矩阵
for i in range(2, n+1):
    for j in range(1, n-i+2):
        C[j-1, i-1] = (C[j, i-2]-C[j-1, i-2])/(X[j+i-2]-X[j-1])

# 取顶端元素作为系数
for i in range(1, n+1):
    c = C[0, i-1]
    print("x为：\n", X[i-1])
    print("系数为：", c)