# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 18:39
# @Author  : Zhang
# @FileName: do_sum.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
from flask import Flask
app = Flask(__name__)


@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    sum = a + b
    return "a + b = %d" % sum


if __name__ == '__main__':
    app.run(debug=True, port=80)





