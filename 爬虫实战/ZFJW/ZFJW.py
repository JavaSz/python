# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 19:55
# @Author  : Zhang
# @FileName: ZFJW.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
import requests
import bs4
import os
# 这是Python的一个非常有名的图片库，这里我们用它来显示验证码
from PIL import Image


def get_post_data(url):
    html = requests.get(url)

    soup = bs4.BeautifulSoup(html.text, 'lxml')

    # 找到验证参数
    __VIEWSTATE = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']

    # 下载验证码图片
    pic = requests.get(
        'http://220.178.71.156:85/(gxv2le55n4jswm45mkv14o2n)/CheckCode.aspx').content
    with open('ver_pic.png', 'wb') as f:
        f.write(pic)

    # 打开验证码图片
    image = Image.open('{}/ver_pic.png'.format(os.getcwd()))
    image.show()

    # 构造需要post的参数表
    data = {'TextBox1': '',
            'Textbox2': '',
            'TextBox3': '',
            '__VIEWSTATE': '',
            # 以学生登录
            'RadioButtonList1': '\xd1\xa7\xc9\xfa',
            'Button1': '',
            'lbLanguage': '', }

    # 构造登录的post参数
    data['__VIEWSTATE'] = __VIEWSTATE
    data['TextBox3'] = input('请输入图片中的验证码')
    data['TextBox1'] = input("请输入学号")
    data['TextBox2'] = input("请输入密码")

    return data


# 登录教务系统
def login(url, data):
    # 通过requests库构造一个浏览器session，这能帮我们自动、持久的管理cookies，
    s = requests.session()
    s.post(url, data=data)
    return s


base_url = 'http://220.178.71.156:85/(g2ym3i3rardh2d55w1vzawrh)/default2.aspx'
data = get_post_data(base_url)
# print(data)
# 模拟登录教务系统
brow = login(base_url, data)
test = brow.get(
    'http://220.178.71.156:85/(g2ym3i3rardh2d55w1vzawrh)/xs_main.aspx?xh=150403126')

# 测试看看是否能找到登陆后的信息
soup = bs4.BeautifulSoup(test.text, 'lxml')
try:
    welcome = soup.find('span', attrs={'id': "Label3"}).text
    name = soup.find('span', attrs={'id': 'xhxm'}).text
except:
    welcome = 'fail'
    name = '登录失败 '
print(welcome + name)
