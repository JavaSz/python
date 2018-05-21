# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 19:55
# @Author  : Zhang
# @FileName: ZFJW.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
import requests
import bs4
import os
import re
# 这是Python的一个非常有名的图片库，这里我们用它来显示验证码
from PIL import Image
from pyquery import PyQuery as pq


headers = {
        "Host": "220.178.71.156:85",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cookie": "td_cookie=2513233523; td_cookie=2512371738"
    }


def save_txt(text, data, col):
    '''
    存储分析结果
    :param text: 文件保存目录
    :param data: 分析结果
    :param col: 列数目
    :return:
    '''

    res = ''
    for i in range(0, len(data)):
        res = res + ('%s\t') % data[i]
        if (i+1) % col == 0 and i > 0:
            res = res + '\n'
    fw = open(text, 'a')
    fw.write(res)
    fw.close()


def get_scores(txt, data, col):
    '''
    解析HTML,获取成绩数据
    :param txt: 文件保存目录
    :param data: HTML数据源
    :param col: 列数目
    :return:
    '''

    pResult = pq(data)
    print(pResult('tr'))
    data_result = []
    for dat in pResult('tr'):
        if len(dat) == col:
            for i in range(len(dat)):
                xxx = pq(dat).find('td').eq(i).text().strip()
                print(xxx)
                data_result.append(xxx)
    save_txt(txt, data_result, col)


def get_post_data(url):
    html = requests.get(url, headers=headers)
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
    data = {
            'TextBox1': '',
            'Textbox2': '',
            'TextBox3': '',
            '__VIEWSTATE': '',
            # 以学生登录
            'RadioButtonList1': '\xd1\xa7\xc9\xfa',
            'Button1': '',
            'lbLanguage': '',
}

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


base_url = 'http://220.178.71.156:85/(tpz4avigqtgxvf45l324xrej)/default2.aspx'
data = get_post_data(base_url)
# print(data['TextBox1'])
# 模拟登录教务系统
brow = login(base_url, data)
test = brow.get(
    'http://220.178.71.156:85/(tpz4avigqtgxvf45l324xrej)/xs_main.aspx?xh=%s' % data['TextBox1'])
# print(test.text)

ScoresURL = r'href="xscjcx.aspx\?([^<]*)" target'
res = re.findall(ScoresURL, test.text)

# 验证登录是否成功
if res:
    username = res[0].split('&')[1].replace('xm=', '')
    url = res[0]
    print(username, u'登录成功！')
else:
    print(u'登录失败，请重新登录！')
    url = ''

Score_url = r'http://220.178.71.156:85/(tpz4avigqtgxvf45l324xrej)/xscjcx.aspx?%s' % url.encode('gb2312')
# print(Score_url)
# headers["Referer"] = r'http://220.178.71.156:85/(tpz4avigqtgxvf45l324xrej)/xs_main.aspx?xh=%s' % data['TextBox1']
# print(headers)
Score_urls = r'http://220.178.71.156:85/(tpz4avigqtgxvf45l324xrej)/xs_main.aspx?xh=%s' % data['TextBox1']
# print(Score_urls)
s = requests.session()
sg = s.get(url=Score_urls, headers=headers).text
# print(sg)
rex2 = 'name="__VIEWSTATE" value="([\S]+)" />'
vs = re.findall(rex2, sg)
print(vs)
scoreData = {
        '__EVENTARGUMENT': '',
        '__EVENTTARGET': '',
        '__VIEWSTATE': vs,
        'hidLanguage': '',
        'ddlXN': '',
        'ddlXQ': '',
        'ddl_kcxz': '',
        'btn_zcj': r'历年成绩'
    }
headers["Referer"] = Score_url
# print(headers)
scorePage = s.post(url=Score_urls, data=scoreData, headers=headers).content
print(scorePage)
get_scores('scores.txt', scorePage, 15)

