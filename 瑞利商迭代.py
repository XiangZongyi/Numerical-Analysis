import numpy as np

A = np.array([[10,-12,-6],[5,-5,-4],[-1,0,3]])
n1, n2, n3 = eval(input("输入初始值："))
x0 = np.array([[n1], [n2], [n3]])

for i in range(4):
    u = x0/np.linalg.norm(x0, 2)
    lamda = np.dot(np.transpose(u), np.dot(A, u))
    x = np.linalg.solve(A-lamda*np.eye(3), u)
    x0 = x

u1 = x/np.linalg.norm(x, 2)
lamda = np.dot(np.transpose(u1), np.dot(A, u1))
print("特征值为：", lamda)