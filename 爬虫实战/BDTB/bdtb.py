import requests
import re

'''
# @Date    : 2018-01-17 16:33:06
# @Author  : zlz (codecool97@gmail.com)
# @Link    : https://www.codedraw.cn
'''

class BDTB:

    def __init__(self):
        self.baseURL = "https://tieba.baidu.com/p/"
        self.seeLZ = '?see_lz='
        self.file = None
        self.default_title = "未命名"
        # 将要读取的页数
        self.page_index = 1
        # 打印的楼层的层数
        self.content_num = 1

    #     页面内容获取
    def get_page(self, question_num, see_lz=1, pn=1):
        try:
            url = self.baseURL + str(question_num) + self.seeLZ +  str(see_lz) + '&pn=' + str(pn)
            r = requests.get(url, timeout=3)
            return r.text
        except Exception as e:
            return e

    # 获得帖子标题
    def get_Title(self, html):
        pattern = re.compile('''<h3.*?>(.*?)</h3>''', re.S)
        # re.S。它表示“.”不包含外侧双引号
        result = re.search(pattern, html)
        if result:
            # print(result.group(1))  # 测试输出
            return result.group(1)
        else:
            return None

        # 获取帖子一共有多少页
    def getPageNum(self, html):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, html)
        if result:
            # print(result.group(1))  #测试输出
            # group()用来提出分组截获的字符串，()用来分组
            return int(result.group(1).strip())
        else:
            return None

    # 获取每一层楼的内容,传入页面内容
    def getDetail(self, html):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        details = re.findall(pattern, html)
        if details:
            str_contents = self.replace(details)
            return str_contents
        return None

    # 取出无用信息
    def replace(self, result):
        str_contents = []
        for detail in result:
            item = re.sub('''<img.*?>|<br>''', "\n", detail)  # 去图片
            item = re.sub('''<a href.*?>|</a>| {4,7}''', "", item)  # 去链接
            str_contents.append(item.strip())
        # print(str_contents)
        return str_contents

    def open_file(self, title):
        if title:
            self.file = open(title + ".txt", "w+", encoding="utf-8")
        else:
            self.file = open(self.default_title + "w+", encoding="utf-8")

    def write_file(self, str_contents):
        for str_content in str_contents:
            self.file.write("楼数：" + str(self.page_index) + "-------------------------------\n")
            self.file.write(str_content + "\n")
            self.page_index += 1

    def start(self, question_num, see_lz=1):
        html = self.get_page(question_num, see_lz, self.page_index)
        title = self.get_Title(html)
        page_num = self.getPageNum(html)
        self.open_file(title)
        # 打印所有页 写入文件
        for i in range(page_num):
            str_contents = self.getDetail(html)
            self.write_file(str_contents)
            self.page_index += 1
            html = self.get_page(question_num, see_lz, self.page_index)


if __name__ == "__main__":
    # baseUrl = 'http://tieba.baidu.com/p/3138733512'
    # bdtb = BDTB(baseUrl, 1)
    # bdtb.getDetail(bdtb.get_page(1))
    # # bdtb.getPageNum()
    bdtb = BDTB()
    bdtb.start(input('请输入你要查询的帖子代码:'), input('只看楼主? 1真0假'))