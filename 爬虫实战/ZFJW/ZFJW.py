# -*- coding: gb2312 -*-
# @Time    : 2018/3/7 19:55
# @Author  : Zhang
# @FileName: ZFJW.py
# @Software: PyCharm
# @Blog    ��https://codedraw.cn
import requests
import bs4
import os
import re
# ����Python��һ���ǳ�������ͼƬ�⣬����������������ʾ��֤��
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
    �洢�������
    :param text: �ļ�����Ŀ¼
    :param data: �������
    :param col: ����Ŀ
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
    ����HTML,��ȡ�ɼ�����
    :param txt: �ļ�����Ŀ¼
    :param data: HTML����Դ
    :param col: ����Ŀ
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

    # �ҵ���֤����
    __VIEWSTATE = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']

    # ������֤��ͼƬ
    pic = requests.get(
        'http://220.178.71.156:85/(gxv2le55n4jswm45mkv14o2n)/CheckCode.aspx').content
    with open('ver_pic.png', 'wb') as f:
        f.write(pic)

    # ����֤��ͼƬ
    image = Image.open('{}/ver_pic.png'.format(os.getcwd()))
    image.show()

    # ������Ҫpost�Ĳ�����
    data = {
            'TextBox1': '',
            'Textbox2': '',
            'TextBox3': '',
            '__VIEWSTATE': '',
            # ��ѧ����¼
            'RadioButtonList1': '\xd1\xa7\xc9\xfa',
            'Button1': '',
            'lbLanguage': '',
}

    # �����¼��post����
    data['__VIEWSTATE'] = __VIEWSTATE
    data['TextBox3'] = input('������ͼƬ�е���֤��')
    data['TextBox1'] = input("������ѧ��")
    data['TextBox2'] = input("����������")

    return data


# ��¼����ϵͳ
def login(url, data):
    # ͨ��requests�⹹��һ�������session�����ܰ������Զ����־õĹ���cookies��
    s = requests.session()
    s.post(url, data=data)
    return s


base_url = 'http://220.178.71.156:85/(tpz4avigqtgxvf45l324xrej)/default2.aspx'
data = get_post_data(base_url)
# print(data['TextBox1'])
# ģ���¼����ϵͳ
brow = login(base_url, data)
test = brow.get(
    'http://220.178.71.156:85/(tpz4avigqtgxvf45l324xrej)/xs_main.aspx?xh=%s' % data['TextBox1'])
# print(test.text)

ScoresURL = r'href="xscjcx.aspx\?([^<]*)" target'
res = re.findall(ScoresURL, test.text)

# ��֤��¼�Ƿ�ɹ�
if res:
    username = res[0].split('&')[1].replace('xm=', '')
    url = res[0]
    print(username, u'��¼�ɹ���')
else:
    print(u'��¼ʧ�ܣ������µ�¼��')
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
        'btn_zcj': r'����ɼ�'
    }
headers["Referer"] = Score_url
print(headers)
scorePage = s.post(url=Score_urls, data=scoreData, headers=headers).content
# print(scorePage)
get_scores('scores.txt', scorePage, 15)

