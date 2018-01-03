import requests, os

kv = {'user-agent': 'Mozilla/6.0'}
root = "F:/pics/"

url = "http://v.stu.126.net/mooc-video/nos/mp4/2017/02/28/1005856317_0295ef32a945401198b0240589e7c84e_shd.mp4?ak=3c4a6205378aa9f4a055c34e040dbfc33d1ad4f9382b90fdb8d96bf76658b71f357dd1ac70171f007df7427bf7a0fbbfeff6a55d15491982836e42383e13363e1ebbeebc312c080f1ec85d32fa63f7d51e46d140b7b30f910299bee40b26a5c2d9e1e3c44585e5de5b539ccdbe8423a821b91261e44e538d2765af73aa008299a7f5cc498d43fe59a782bc973c30c066b767da1f870bc890754ea6567cb70ca9830b67d08aac63e1ac0c534090a89323f6fd9d4e9030d5d8cb0cb4b5fcb8e77c"
path = root + url.split('/')[-1].split('?')[0]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print("文件已存在")
except Exception as e:
    print('爬取失败', e)

# r.raise_for_status()
# r.encoding=r.apparent_encoding
# print(r.text[:1000])