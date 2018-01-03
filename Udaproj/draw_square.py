# -*-coding:utf-8 -*-
import turtle


def draw_square(turtle_one):
    for i in range(0, 4):
        turtle_one.forward(100)
        turtle_one.right(90)


def code_draw():
    window = turtle.Screen()  # 添加一个窗口
    window.bgcolor("White")  # 设置窗口的背景颜色
    # 创建第一个对象画正方形
    Taylor = turtle.Turtle()
    Taylor.shape("turtle")
    Taylor.color("Red")
    Taylor.speed(10)
    for i in range(0, 36):
        draw_square(Taylor)
        Taylor.right(10)
    window.exitonclick()

code_draw()