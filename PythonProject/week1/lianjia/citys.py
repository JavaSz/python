# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 20:12
# @Author  : Zhang
# @FileName: citys.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
import csv
from bs4 import BeautifulSoup
import requests


r = requests.get("https://www.lianjia.com")
demo = r.text
# print(demo)
soup = BeautifulSoup(demo, "html5lib")
# print(soup)
citys = soup.find("div", {"class": "all"})
city = citys.findChildren("a")
# print(city)


# 将数据保存
with open("citys.csv", "w") as f:
    writ = csv.writer(f)
    for city in city:
        # 获取 <a> 标签的 href 链接
        city_url = city.get("href")
        # 获取 <a> 标签的文字，如:合肥
        city_name = city.get_text()
        writ.writerow((city_name, city_url))
        print(city_name, city_url)




