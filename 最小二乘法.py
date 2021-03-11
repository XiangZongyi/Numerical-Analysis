import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,0.59],[1,0.80],[1,0.95],[1,0.45],[1,0.79],[1,0.99],[1,0.90],[1,0.65],[1,0.79],[1,0.69],[1,0.79],
             [1,0.49],[1,1.09],[1,0.95],[1,0.79],[1,0.65],[1,0.45],[1,0.60],[1,0.89],[1,0.79],[1,0.99],[1,0.85]])
b = np.array([[3980],[2200],[1850],[6100],[2100],[1700],[2000],[4200],[2440],[3300],[2300],
             [6000],[1190],[1960],[2760],[4330],[6960],[4160],[1990],[2860],[1920],[2160]])
A_ = np.dot(np.transpose(A), A)
b_ = np.dot(np.transpose(A), b)
c = np.linalg.solve(A_, b_)
error = b-np.dot(A,c)
SE = 0
for i in range(len(error)):
    SE = SE + error[i]**2
RMSE = (SE/len(error))**0.5
print('系数c1,c2分别为：',c)
print('均方误差为：',RMSE)

# 画图
X = A[:, 1]
Y = b
plt.scatter(X,Y,c='green')
x = np.arange(0,1,0.01)
y = c[0]+c[1] * x
plt.rcParams['font.sans-serif']=['SimHei']
plt.title('最小二乘直线方程')
plt.xlabel('价格')
plt.ylabel('销量/周')
plt.plot(x,y)
plt.show()

Z = []
list(X)
c1 = float(c[0])
c2 = float(c[1])
for j in range(len(X)):
    x0 = X[j]
    z = (c1+c2*x0)*(x0-0.25)
    Z.append(z)
Z1 = np.array(Z)
Z2 = Z1.argsort()
a = Z2[-1]
print("利润最大化的销售价格为：", X[a])




