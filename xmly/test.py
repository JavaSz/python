#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/16 15:49
# @Author  : Aries
# @Site    :
# @File    : main.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
import os

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}
# 通过列表推导式生成待采集列表
def get_url(url):
    start_urls = [url.format(pn) for pn in range(1,2) ]
    print(start_urls)
#     遍历列表内的URL
    for list_url in start_urls:
        html = requests.get(list_url,headers=headers).text
        soup = BeautifulSoup(html,'lxml')
        # 遍历当前页面的专辑div块
        for item in soup.find_all(class_ = 'albumfaceOutter'):
            content = {
                'href':item.a['href'],# 获取每个专辑的URL
                'title':item.img['alt'],# 专辑名称
                'img':item.img['src']# 专辑封面
            }
            # 此处可以进行入库处理
            get_m4a(content)
            break # 测试方便，这里只循环一次

# 进入频道封面页
def get_m4a(url):
    html = requests.get(url['href'],headers=headers).text
    # 获取音频ID列表
    m4a_url_list = etree.HTML(html).xpath('//div[@class="personal_body"]/@sound_ids')[0].split(',')
    print(u'本频道存在{}个音频'.format(str(len(m4a_url_list))))
    for m4a_id in m4a_url_list:
        m4a_url = 'http://www.ximalaya.com/tracks/{}.json'.format(m4a_id)
        html = requests.get(m4a_url,headers=headers).text # content返回的是二进制
        # 转换为字典
        re = json.loads(html)
        # print re['play_path']
        # 下载文件
        m4a_file = requests.get(re['play_path'],headers=headers).content
        with open('%s\\%s.m4a' %(url['title'],m4a_id),'wb') as f:
            f.write(m4a_file)
            print(u'下载成功,文件ID为:{}'.format(m4a_id))

print(__name__)
if __name__ == '__main__':
    start_url = 'http://www.ximalaya.com/dq/{}'
    get_url(start_url)