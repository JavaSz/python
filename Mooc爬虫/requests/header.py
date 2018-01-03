import requests
# r = requests.head("http://httpbin.org")
# print(r.headers)  # 获取目标URL头部字段

# a = requests.put("http://httpbin.org/put", data="ABC")

# print(a.text)  # 当传入的是一个字符串的时候默认放在data下

putlist = {"key1": "One", "key2": "Two"}
r = requests.put("http://httpbin.org/put", data=putlist)  # 当传入的是一个数组的时候放在form表单中

print(r.text)
