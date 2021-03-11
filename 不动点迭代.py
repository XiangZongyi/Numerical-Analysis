import math
x0 = float(input("输入初始估计值："))
k = int(input("输入迭代次数："))
g = lambda x: 1-5*x+7.5*x**2-2.5*x**3

def FPI(g, x0, k):
    for i in range(k):
        x = g(x0)
        x0 = x
    return x
x = FPI(g, x0, k)
print("方程的解为：", x)
