# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 17:46
# @Author  : Zhang
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
from flask import Flask
app = Flask(__name__)


@app.route('/index')  # route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数。
def hello_world():
    return 'my Name!'


@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户的名称
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    return 'Post %d' % post_id


@app.route('/project/')
def project():
    return 'the project page'


@app.route('/about')
def about():
    return 'the about page'


if __name__ == '__main__':
    app.run(debug=True)
