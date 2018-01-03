import requests
# 爬取amazon商品信息
# 模拟浏览器请求
url = 'https://www.amazon.cn/dp/B00CIHXOOM'
user_agent = {'User-Agent': 'Chrome/63.0.3239.84'}
try:
    r = requests.get(url, headers=user_agent)
    r.raise_for_status()
    print(r.text[:1000])
    print("爬取成功")
    print(r.request.headers)  # 看一下我们请求时发送的头部信息 'User-Agent': 'python-requests/2.18.4'
    # 修改headers之后 可以看到 我们发送的请求 中的user-agent字段已经变成了Chrome/63.0.3239.84

except:
    print("爬取失败")

# 此时爬取成功
