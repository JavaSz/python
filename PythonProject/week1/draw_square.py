# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 18:57
# @Author  : Zhang
# @FileName: draw_square.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
import turtle, time

turtle.setup(2000, 2000, 0, 0)
turtle.pensize(20)
turtle.pencolor("black")
turtle.seth(0)
length = 400
angle = 0
for i in range(5):
    turtle.fd(length)
    angle = angle - 144
    turtle.seth(angle)

time.sleep(10)