# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 22:26
# @Author  : Zhang
# @FileName: house.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
import sys
import re
import csv
import requests
from bs4 import BeautifulSoup


# 成功打开页面时返回页面对象，否则打印错误信息，退出程序
url = "https://hf.lianjia.com/ershoufang/shushan/"


def get_soup(url):
    r = requests.get(url)
    # 状态码为 200 时页面成功打开
    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, "html5lib")
        return soup
    else:
        print("页面错误")
        sys.exit()


# 将页面中每一条房屋信息保存为一个字典，将所有的字典保存在列表中，返回列表
def get_house_info_list(url):
    house_info_list = []
    soup = get_soup(url)
    if not soup:
        return None

    house_list = soup.find_all("li", {"class": "clear"})

    for house in house_list:
        # 标题
        title = house.find("div", {"class": "title"}).get_text()

        # 获取信息数据（例：大溪地天润轩 | 3室2厅 | 102平米 | 南 北 | 毛坯），通过“|”符号分割字符串
        info = house.find("div", {"class": "houseInfo"}).get_text().split("|")

        # 小区（例：大溪地天润轩），strip()去除字符串两边的空格，encode，将字符串编码成 utf-8 格式
        block = info[0].strip()

        # 房型（例：2室一厅）
        house_type = info[1].strip()

        # 面积大小
        size_info = info[2].strip()
        size = re.findall(r"\d+", size_info)[0]

        # 价格
        price_info = house.find("div", {"class": "totalPrice"}).span.get_text()
        price = re.findall(r"\d+", price_info)[0]
        # print(price)

        # 添加到列表中
        house_info_list.append({
            "title": title,
            "price": int(price),
            "size": int(size),
            "block": block,
            "house_type": house_type
        })
    return house_info_list


# 读取前三个页面的房屋信息，将信息保存到 house.csv 文件中
def house(url):
    house_info_list = []

    # range(3),即前三个子页面
    for i in range(3):
        new_url = url + 'pg' + str(i+1)
        house_info_list.extend(get_house_info_list(new_url))

    if house_info_list:
        # 将数据保存到 house.csv 文件中
        with open("./house.csv", "w+") as f:
            # writer 对象，修改默认分隔符为 "|"
            writer = csv.writer(f, delimiter="|")
            for house_info in house_info_list:
                title = house_info.get("title")
                price = house_info.get("price")
                size = house_info.get("size")
                block = house_info.get("block")
                house_type = house_info.get("house_type")
                # 写入一行
                writer.writerow([str(title), int(price), int(size), str(block), str(house_type)])
                print(block, price, size)
