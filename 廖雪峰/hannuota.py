# 汉诺塔


def move(n, a, b, c):
    if n == 1:
        print(a, '--->', c)
    else:
        move(n-1, a, c, b)
        print(a, '--->', c)
        move(n-1, b, a, c)


print('本程序的目的就是把A柱子上的汉诺塔圆盘借助于B柱子按照原来的上下次序放到C柱子上的过程显示出来')
num = int(input('请输入A柱子上圆盘的个数：'))


print(move(num, 'A', 'B', 'C'))
