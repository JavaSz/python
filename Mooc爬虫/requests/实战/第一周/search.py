import requests
# 向百度/360提交关键字 并返回查询结果
# 关键词接口
# 百度: http://www.baidu.com/s?wd=<keyword>
# 360: http://www.so.com/s?q=<keyword>
keyword = {'wd': 'Google'}
url = "http://www.baidu.com/s"
try:
    r = requests.get(url, params=keyword)
    r.raise_for_status()
    print(r.request.url)  # 查询当前的提交给百度的链接
    print(len(r.text))
    print(r.text[100:1000])
    print("查询成功")
except:
    print("查询失败")
