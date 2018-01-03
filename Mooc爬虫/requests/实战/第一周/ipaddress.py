import requests
# 自动查询IP地址
url1 = "http://m.ip138.com/ip.asp"
url2 = "http://m.ip138.com/mobile.asp"
keyword1 = {"ip": "183.232.231.172"}
keyword2 = {"mobile": "15855834240"}
try:
    r = requests.get(url1, params=keyword1)
    r.raise_for_status()
    # r.encoding = r.apparent_encoding
    print("你要查询的IP地址归属地为:"+r.text)
    # p = requests.get(url2, params=keyword2)
    # print(p.text)
except Exception as e:
    print("爬取失败", e)
