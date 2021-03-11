import numpy as np

A = np.array([[10,-12,-6],[5,-5,-4],[-1,0,3]])
x0 = np.array([[1],[1],[1]])

for i in range(100):
    u = x0/np.linalg.norm(x0, 2)
    x = np.dot(A, u)
    x0 = x

u1 = x0/np.linalg.norm(x0, 2)
lamda = np.dot(np.dot(np.transpose(u1), A), u1)
print("特征值为：", lamda)
print("特征向量：", u1)

