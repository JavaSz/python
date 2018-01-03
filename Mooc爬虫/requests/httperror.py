# -*- coding:utf-8 -*-
import requests
import sys
import io


def getHtmlText(url):
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 获取异常码
        r.encoding = r.apparent_encoding
        return r.text
    except:  # 检测到异常之后执行
        return "产生异常"


if __name__ == "__main__":
    url = "https://www.google.com"
    print(getHtmlText(url))
