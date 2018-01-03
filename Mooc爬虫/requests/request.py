# requests.request(method, url, **kwargs)
import requests
'''
params:字典或者字节序列,作为参数传入到目标url中
服务器可以接收这些参数,筛选部分资源
'''
key_value = {"Username": "One", "Password": "Two"}
r = requests.request('GET', 'https://www.codedraw.cn/ws', params=key_value)
print(r.url)
# '''
# data:字典、字节序列或文件对象,作为request的内容
# '''
# key_value1 = {"Username": "One", "Password": "Two"}
# re = requests.request('POST', 'https://www.codedraw.cn/ws', data=key_value1)
# body = "内容"
# re = requests.request('POST', 'https://www.codedraw.cn/ws', data=body)
'''
JSON:传入参数,服务器赋值到JSON文件中
'''
# key_value1 = {"Username": "One", "Password": "Two"}
# re = requests.request('POST', 'https://www.codedraw.cn/ws', json=key_value1)
'''
headers:字典,HTTP定制头
向服务器请求时,可以模拟为你定义的浏览器版本来请求数据
'''
hds = {'User-Agent': 'Chrome/63.0.3239.84 Safari/537.36'}
req = requests.request('POST', 'https://www.codedraw.cn/ws', headers=hds)
'''
cookies:字典或CookieJar,Request中的cookie
auth:元组,支持HTTP认证功能
timeout:设置超时时间 秒为单位
file:字典类型,向服务器传输文件
'''
file = {'file': open('filename', 'rb')}
r = requests.request('POST', 'https://www.codedraw.cn/file', files=file)
'''
proxies:字典类型,设定访问url的代理服务器,可以有效的隐藏你的IP地址
'''
daili = {'http': '10.10.10.10', 'https': '10.10.1.1'}
r = requests.request('POST', 'https://www.codedraw.cn/', proxies=daili)
'''
allow_redirects: True/False 默认True 允不允许对url重定向
stream: True/False 默认True 是否对获取的内容立即下载
verify: True/False 默认True 是否认证SSL证书
cert: 本地SSL证书路径
'''
















