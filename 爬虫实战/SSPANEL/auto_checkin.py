# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 20:02
# @Author  : Zhang
# @FileName: auto_checkin.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

base_url = 'https://fly.bgp.sh'


def checkin():
    email = input('请输入您的邮箱: ')
    password = input('请输入您的密码: ')

    email = email.split('@')
    email = email[0] + '%40' + email[1]

    session = requests.session()
    login_url = base_url + '/auth/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    post_data = 'email=' + email + '&passwd=' + password + '&code=&remember_me=week'
    post_data = post_data.encode()
    response = session.post(login_url, post_data, headers=headers, verify=False)
    # 签到
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Referer': base_url + '/user'
    }

    response = session.post(base_url + '/user/checkin', headers=headers)


while True:
    try:
        checkin()
        print("恭喜你,签到成功")
    except Exception:
        continue
    break