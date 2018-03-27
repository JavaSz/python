# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 19:57
# @Author  : Zhang
# @FileName: calculator.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn


# 输入字符串处理
class Buffer(object):
    def __init__(self, data):
        self.data = data
        self.offset = 0

    # 提取offset位置处的一个字符
    def peek(self):
        # 如果没有后续字符则返回None
        if self.offset >= len(self.data):
            return None
        return self.data[self.offset]

    # 取字符的位置向后移动一位
    def advance(self):
        self.offset += 1
