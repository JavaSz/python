# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 20:03
# @Author  : Zhang
# @FileName: lianjia_spider.py
# @Software: PyCharm
# @Blog    ：https://codedraw.cn
import csv
import sys
import requests
from bs4 import BeautifulSoup
from house import house
import time


def get_city_dict():
    # 创建一个dict 用于存储city信息
    city_dict = {}
    with open("citys.csv", "r") as f:
        reader = csv.reader(f)  # 获取csv内容
        # print(reader)
        # 将reader中的信息 存储到dict中
        for city in reader:
            # print(city)
            city_dict[city[0]] = city[1]
    return city_dict


# 将城市对应的区域信息保存到字典中
def get_area_dict(url):
    # 将信息保存到字典中
    area_dict = {}
    r = requests.get(url)
    demo = r.text
    soup = BeautifulSoup(demo, "html5lib")
    # 容器 <div data-role="ershoufang"> 下的每一个 <a> 标签对应一条信息
    tags = soup.find("div", {"data-role": "ershoufang"}).findChildren("a")

    """
    tags 内数据的格式如下
            <a href="/ershoufang/shushan/"  title="合肥蜀山在售二手房 ">蜀山</a>
            <a href="/ershoufang/luyang/"  title="合肥庐阳在售二手房 ">庐阳</a>
            <a href="/ershoufang/yaohai/"  title="合肥瑶海在售二手房 ">瑶海</a>
            ...

    """

    for tag in tags:
        # 对应区域的 url
        area_url = tag.get("href")
        # 对应区域的名称
        area_name = tag.get_text()
        # 保存在字典中
        area_dict[area_name] = area_url
    return area_dict


def run():

    city_dict = get_city_dict()
    # 打印城市名
    for city in city_dict.keys():
        print(city)
    print()

    input_city = input("请输入要查询的城市：")
    city_url = city_dict.get(input_city)

    # 输入错误，退出程序
    if not city_url:
        print("请检查是否存在该区域")
        sys.exit()
    ershoufang_city_url = city_url + "ershoufang"
    district_dict = get_area_dict(ershoufang_city_url)

    # 打印区域名
    for district in district_dict.keys():
        print(district)
    print()

    input_district = input("请输入你要查询的地区:")
    district_url = district_dict.get(input_district)

    # 输入错误，退出程序
    if not district_url:
        print("请检查区域列表中是否含有该区域")
        sys.exit()

    # 如果都输入正确
    house_info_url = city_url + district_url[1:]
    # print(house_info_url)
    print("以下信息 分别代表 小区名称 面积 金额/万 ")
    house(house_info_url)
    time.sleep(1000)


if __name__ == "__main__":
    run()








