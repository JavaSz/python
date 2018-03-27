# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 19:12
# @Author  : Zhang
# @FileName: draw_snake.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
import turtle, time, random


def draw_snake(radius, angle, len, neckrad):
    # random color list
    color_list = ["#611581", "#00695b", "#FFB6C1", "#4B0082", "#c40000", "#FFFF00", "#ADFF2F"]
    for i in range(len):
        color = color_list[random.randint(0, 6)]
        turtle.pencolor(color)
        turtle.circle(radius, angle)
        turtle.circle(-radius, angle)
    turtle.circle(radius, angle / 2)
    turtle.forward(radius)
    turtle.circle(neckrad + 1, 180)
    turtle.fd(radius * 2 / 3)


def main():
    turtle.setup(1300, 800, 0, 0)
    draw_size = 20
    turtle.pensize(draw_size)
    turtle.seth(10)
    draw_snake(40, 80, 4, draw_size / 2)


main()
time.sleep(3)
