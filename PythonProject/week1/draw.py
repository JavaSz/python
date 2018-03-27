# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 17:19
# @Author  : Zhang
# @FileName: draw.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
import turtle, time


def draw_snake(radius, angle, len, neckrad):
    # radius 圆半径 angle 圆弧度
    turtle.hideturtle()  # 隐藏箭头
    for i in range(len):
        turtle.circle(radius, angle)
        turtle.circle(-radius, angle)
    turtle.circle(radius, angle / 2)
    turtle.forward(radius)
    turtle.circle(neckrad + 1, 180)
    turtle.fd(radius * 2 / 3)


def main():
    turtle.setup(1300, 800, 0, 0)
    draw_size = 20
    turtle.pensize(draw_size)  # 控制线条粗细
    turtle.pencolor("blue")  # control pencolor
    turtle.seth(10)  # 设置起始角度
    draw_snake(40, 80, 4, draw_size / 2)


main()
# wait for 3 sec
time.sleep(3)
