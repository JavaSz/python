import math
import types


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def quadratic(a, b, c):  # 求一元二次方程
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1, x2


def power(x, n=2):  # 求x的n次方
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def product(*x):  # 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
    s = 1
    if x == ():
        raise TypeError('at least one parameter')
    else:
        for i in x:
            if not ((type(i) == type(1)) | (type(i) == type(0.1))):
                raise TypeError('All parameters must be an integer or a floating-point number')
        for i in x:
            s = s * i
    return s
