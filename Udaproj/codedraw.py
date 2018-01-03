# -*-coding:utf-8 -*-
# 如何用python来画一个正方形
import turtle


def draw_square():
    window = turtle.Screen()  # 添加一个窗口
    window.bgcolor("blue")  # 同时将窗口的背景颜色定义为蓝色

    Taylor = turtle.Turtle()  # 定义一个对象为Taylor
    Taylor.shape("turtle")  # .shape方法可以自定义Turtle的形状
    Taylor.color("Red")  # .color方法可以自定义Turtle的颜色
    Taylor.speed(1)  # turtle.speed()：设置绘制的速度，1-10，1最慢，10最快；
    Taylor.forward(100)  # 让Taylor向前移动100个像素
    Taylor.right(90)  # 右转90度
    Taylor.forward(100)  # 让Taylor向前移动100个像素
    Taylor.right(90)  # 右转90度
    Taylor.forward(100)  # 让Taylor向前移动100个像素
    Taylor.right(90)  # 右转90度
    Taylor.forward(100)  # 让Taylor向前移动100个像素
    Taylor.right(90)  # 右转90度


    Swift = turtle.Turtle()  # 再定义一个Swift继续画图
    Swift.shape("arrow")  # 箭头形状定为三角形
    Swift.color("Pink")  # 粉色
    Swift.circle(100)

    window.exitonclick()  # 点击窗口即可结束程序


draw_square()
