# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 18:14
# @Author  : Zhang
# @FileName: url.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
from flask import Flask,url_for
app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'


@app.route('/login')
def login():
    return 'login page'


@app.route('/user/<username>')
def profile(username):
    return username


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


if __name__ == "__main__":
    app.run(debug=True)
