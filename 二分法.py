import numpy as np
def bisect(a, b, A):
    fa = a*a - A
    fb = b*b - A
    n = 0 #计算迭代次数
    while (b-a)/2 > 1e-8:
        c = (a+b)/2
        fc = c*c - A
        if fc == 0:
            return c
        if (np.sign(fc*fa)<0):
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        n = n+1
    print((a+b)/2)
    print(n)
    return

A = int(input("q请输入A的值："))
a = 2
b = 3
bisect(a, b, A)
