# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 19:02
# @Author  : Zhang
# @FileName: render_templates.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
from flask import render_template, Flask
app = Flask(__name__)


@app.route('/hello/')
def hello(): pass


@app.route('/hello/<name>')
def helloname(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, port=80)
