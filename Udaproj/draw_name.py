# -*-coding:utf-8 -*-
import turtle
import math

turtle.color("red")
turtle.ondrag(turtle.goto)  # 手绘turtle
def code_draw():
    window = turtle.Screen()  # 添加一个窗口
    window.bgcolor("White")  # 设置窗口的背景颜色
    # 创建一个对象
    Taylor = turtle.Turtle()
    Taylor.color("red")
    Taylor.shape("turtle")
    Taylor.up()
    Taylor.backward(200)
    Taylor.left(90)
    Taylor.forward(200)
    Taylor.down()
    Taylor.right(90)
    Taylor.forward(100)
    Taylor.right(135)
    Taylor.forward(math.sqrt(math.pow(100, 2) + math.pow(100, 2)))
    # math.sqrt() 求平方根 math.pow(x, y) 求x的y次方
    Taylor.left(135)
    Taylor.forward(100)
    # 第二部分
    Taylor.up()
    Taylor.forward(50)
    Taylor.left(90)
    Taylor.forward(100)
    Taylor.down()
    Taylor.color("blue")
    Taylor.backward(100)
    Taylor.right(90)
    Taylor.forward(80)
    # 第三部分
    Taylor.up()
    Taylor.forward(50)
    Taylor.left(90)
    Taylor.forward(100)
    Taylor.right(90)
    Taylor.down()
    Taylor.color("black")
    Taylor.forward(100)
    Taylor.right(135)
    Taylor.forward(math.sqrt(math.pow(100, 2) + math.pow(100, 2)))
    Taylor.left(135)
    Taylor.forward(100)
    # 附加ONE
    Taylor.up()
    Taylor.home()
    Taylor.backward(200)
    Taylor.right(90)
    Taylor.down()
    Taylor.color("red")
    Taylor.shape("arrow")
    Taylor.left(90)
    Taylor.forward(100)
    Taylor.right(135)
    Taylor.forward(math.sqrt(math.pow(100, 2) + math.pow(100, 2)))
    Taylor.left(135)
    Taylor.forward(100)
    # 附加TWO
    Taylor.up()
    Taylor.forward(50)
    Taylor.left(90)
    Taylor.forward(100)
    Taylor.right(90)
    Taylor.down()
    Taylor.color("blue")
    Taylor.forward(100)
    Taylor.backward(50)
    Taylor.right(90)
    Taylor.forward(100)
    # 附加THREE
    Taylor.up()
    Taylor.left(90)
    Taylor.forward(100)
    Taylor.left(90)
    Taylor.forward(100)
    Taylor.right(90)
    Taylor.down()
    Taylor.color("black")
    Taylor.forward(100)
    Taylor.backward(50)
    Taylor.right(90)
    Taylor.forward(100)
    window.exitonclick()  # 点击结束程序


code_draw()