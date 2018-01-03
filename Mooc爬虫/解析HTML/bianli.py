import requests
from bs4 import BeautifulSoup
# 如何遍历HTML文件
# 下行遍历
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# print(soup.head)  # 查看head标签内容
# print(soup.head.contents)  # .contents可以获取head的子标签 返回的类型是列表
# print(soup.body.contents)  # 查看body标签内容
# print(len(soup.body.contents))  # 查看子元素的数量
# print(soup.body.contents[1])
# for child in soup.body.children:  # 遍历body元素的子元素
#     print(child)
# for childc in soup.body.descendants:  # 遍历body元素的子孙元素
#     print(childc)

'''
上行遍历:.parent 父亲标签 .parents 先辈标签
'''
for parent in soup.a.parents:  # 上行遍历a标签的先辈节点 并输出先辈的名字
    if parent is None:
        print(parent)
    else:
        print(parent.name)
'''
平行遍历:
        .next_sibling 返回按照HTML文本顺序的下一个平行节点标签
        .previous_sibling 返回按照HTML文本顺序的上一个平行节点标签
        .next_siblings 迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
        .previous_siblings 迭代类型 返回按照HTML文本顺序的前续所有平行节点标签
        所有的平行遍历必须发生在同一个父亲节点下
'''
print(soup.a.next_sibling)  # a标签的下一个平行标签
print(soup.a.next_sibling.next_sibling)  # a标签的下一个的下一个平行标签
print(soup.a.previous_sibling)  # a标签的上一个平行标签
for sibling in soup.a.next_siblings:  # 遍历a标签的后续所有平行节点
    print(sibling)
for sibling in soup.a.previous_siblings:  # 遍历a标签的前续所有平行节点
    print(sibling)

'''
迭代类型只能用在 for in :结构中
'''
# 如何使HTML更加友好的显示 .prettify
print(soup.prettify())
# utf-8编码
