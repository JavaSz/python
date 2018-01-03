import requests
from bs4 import BeautifulSoup
# BeautifulSoup库是能够解析HTML和XML的库
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")  # 以html格式解析 html.parser解析器
# print(soup.prettify())  # 输出解析后的代码
# 获取demo.html的title标签
print(soup.title)
# 获取目标url中的a标签
print(soup.a)  # 默认输出一个a标签
print(soup.a.name)  # 获取a标签的名字
print(soup.a.parent.name)  # 获取a标签父元素的名字
print(soup.a.parent.parent.name)  # 获取p标签父元素的名字
print(soup.a.attrs)  # 查看a标签的属性
# 返回了一个数组 假如我们想要提取当中的href字段
print(soup.a.attrs['href'])  # 这是我们就把href字段提取出来了
# 查看标签属性的类型
print(type(soup.a.attrs))  # <class 'dict'> 字典类型
# 提取标签中的字符串信息即内容
print(soup.a.string)
print(soup.p.string)

