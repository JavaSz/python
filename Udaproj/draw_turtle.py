# -*-coding:utf-8 -*-
import turtle


def draw_square(turtle_one):
    for i in range(0, 4):
        turtle_one.forward(100)
        turtle_one.right(90)


def draw_triangle(turtle_three):
    for i in range(0, 3):
       turtle_three.forward(100)
       turtle_three.left(120)

def code_draw():
    window = turtle.Screen()  # 添加一个窗口
    window.bgcolor("White")  # 设置窗口的背景颜色
    # 创建第一个对象画正方形
    Taylor = turtle.Turtle()
    Taylor.shape("turtle")
    Taylor.color("Red")
    Taylor.speed(1)
    draw_square(Taylor)
    # 创建第二个对象来画圆
    Swift = turtle.Turtle()
    Swift.color("Blue")
    Swift.shape("arrow")
    Swift.circle(100)
    # 创建第三个对象来画一个三角形
    MeiMei = turtle.Turtle()
    MeiMei.up()  # 抬笔:不在作画 但行为还要继续进行
    MeiMei.goto(100,0)
    MeiMei.down()  # 继续作画
    # MeiMei.forward(100)
    # MeiMei.left(120)
    # MeiMei.forward(100)
    # MeiMei.left(120)
    # MeiMei.forward(100)
    draw_triangle(MeiMei)
    window.exitonclick()

code_draw()
