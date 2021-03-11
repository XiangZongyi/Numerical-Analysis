import numpy as np
# 搭建矩阵的框架
n = int(input("希尔伯特矩阵的维度n:"))
matrix = np.zeros([n, n])
# 构建希尔伯特矩阵
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[0]):
        matrix[i, j] = 1 / ((i+1) +(j+1) - 1)
# 高斯消元
input_raw_data = matrix
# b 列矩阵
b_data = np.ones([n])
for i in range(matrix.shape[0] - 1):
    for j in range(i + 1, matrix.shape[0]):
        a = matrix[j, i] / matrix[i, i]
        for k in range(i, matrix.shape[0]):
            matrix[j, k] = matrix[j, k] - a * matrix[i, k]
        b_data[j] = b_data[j] - a * b_data[i]
# x 列矩阵
x = np.zeros([b_data.shape[0]])
for p in range(matrix.shape[1] - 1, -1, -1):
    for q in range(p + 1, b_data.shape[0]):
        b_data[p] = b_data[p] - matrix[p, q] * x[q]
    x[p] = b_data[p] / matrix[p, p]
for item in x:
    print("{:.3f}".format(item), end='  ')
