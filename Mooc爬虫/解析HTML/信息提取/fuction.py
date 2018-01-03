from bs4 import BeautifulSoup
import requests
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
for get_link in soup.find_all('a'):
    print(get_link.get('href'))
# 找出a标签下 所有的href链接
# 基于bs4库 <>.find_all(name, attrs, recursive, )
# <>.find_all('p', 'course')
# <>.find_all('p', 'course',true/false) 是否查找该节点下面的所有子孙节点

