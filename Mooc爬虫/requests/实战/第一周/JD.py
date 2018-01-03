import requests
# 爬取JD商品页面 https://item.jd.com/2967929.html
url = 'https://item.jd.com/2967929.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
    print("爬取成功")
except:
    print("爬取失败")


