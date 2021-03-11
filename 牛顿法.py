from math import *
x0 = float(input("输入初始估计值:"))
g = lambda x: x-(54*x**6+45*x**5-102*x**4-69*x**3+35*x**2+16*x-4)/(324*x**5+225*x**4-408*x**3-207*x**2+70*x+16)
k = 100
def newton(g, x0 ,k):
    x = g(x0)
    for i in range(k):
        x0 = x
        x = g(x0)
    return x0
x = newton(g, x0, k)
print("方程的解为：",x)