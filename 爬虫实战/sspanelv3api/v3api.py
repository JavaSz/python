# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 21:47
# @Author  : Zhang
# @FileName: v3api.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

token_url = "http://demo.codedraw.cn/api/token"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}


def get_token():
    email = input('请输入您的邮箱: ')
    password = input('请输入您的密码: ')
    # 暂时不需要
    # email = email.split('@')
    # email = email[0] + '%40' + email[1]
    session = requests.session()
    post_data = 'email=' + email + '&passwd=' + password
    r = session.post(token_url, post_data, headers=headers, verify=False)
    dict = r.json()
    info = dict['data']
    print(info)
    info_url = token_url + '/{}'.format(info['token'])
    user_info_url = 'http://demo.codedraw.cn/api/user/{}?access_token={}'.format(info['user_id'], info['token'])
    e = requests.get(user_info_url, headers)
    # e = requests.get(info_url, headers)
    print(e.text)
    node_url = 'http://demo.codedraw.cn/api/node?access_token={}'.format(info['token'])
    node = requests.get(node_url, headers)
    print(node.text)



if __name__ == '__main__':
    get_token()