# -*-coding:utf-8 -*-
import turtle


def draw_square():
    window = turtle.Screen()  # 添加一个窗口
    window.bgcolor("blue")  # 同时将窗口的背景颜色定义为蓝色

    Taylor = turtle.Turtle()  # 定义一个对象为Taylor
    Taylor.color("Red")  # .color方法可以自定义Turtle的颜色
    Taylor.speed(1)  # turtle.speed()：设置绘制的速度，1-10，1最慢，10最快；
    Taylor.backward(100)  # 后退100个像素
    Taylor.up()  # 抬笔:不在作画 但行为还要继续进行
    Taylor.right(90)  # 右转90度
    Taylor.forward(20)  # 向前20个像素
    Taylor.left(90)  # 左转90度
    Taylor.down()  # 继续作画
    Taylor.forward(100)  # 向前100个像素

    window.exitonclick()  # 点击窗口即可结束程序


draw_square()
