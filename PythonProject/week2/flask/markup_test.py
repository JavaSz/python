# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 19:15
# @Author  : Zhang
# @FileName: markup_test.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
from flask import Markup
print(Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>')
print(Markup.escape('<blink>hacker</blink>'))
print(Markup('<em>Marked up</em> &raquo; HTML').striptags())
