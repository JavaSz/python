import requests
import os
# 爬取图片并存储下来
root = "F://pics//"
url = "http://qblog-10012769.cos.myqcloud.com/xiaochengxu/1.gif"  # 要获取的图片地址
path = root + url.split('/')[-1]  # 用/来分隔元素 同时取倒数第一个元素 从而获取了文件名
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)  #
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")

