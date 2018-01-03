# -*- coding: utf-8 -*-
# hex() 整数-->十六进制
# abs() 绝对值
from __init__ import my_abs
from __init__ import quadratic
from __init__ import power
from __init__ import product
n1 = 255
n2 = 1000
n3 = -10
print(hex(n1))
print(hex(n2))
print(abs(n3))
print(my_abs(-100))
print(quadratic(2, 3, 1))
print(power(5))
print(power(5, 2))

# print('product() =', product())
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# *args list **kw dict
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
