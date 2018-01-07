# 糗事百科 热门段子
import urllib.request
import urllib.error
import re

'''
# @Date    : 2018-01-17 16:33:06
# @Author  : zlz (codecool97@gmail.com)
# @Link    : https://www.codedraw.cn
'''


class QSBK:
    # 初始化方法，定义一些变量
    def __init__(self):
        # 页面
        self.pageIndex = 1
        # headers
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        # 存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False

    # 传入某一页的索引获得页面代码
    def getHtmlText(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            # 构建请求的request
            request = urllib.request.Request(url, headers=self.headers)
            # 利用urlopen获取页面代码
            response = urllib.request.urlopen(request)
            # 将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib.error.URLError as e:
            print("getPage失败")
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
            return None

    def get_duanzi(self, pageIndex):
        html = self.getHtmlText(self.pageIndex)
        # soup = BeautifulSoup(html, 'html.parser')
        # print(soup.find_all('div', class_='content'))
        # 作者信息 内容 配图 点赞数 评论数
        pattern = re.compile('''<div class="article block untagged mb15.*?<h2>(.*?)</h2>'''
                             + '''.*?<span>(.*?)</span>'''
                             + '''.*?<!-- 图片或gif -->(.*?)<div class="stats">'''
                             + '''.*?<span class="stats-vote"><i class="number">(.*?)</i>''', re.S)
        details = re.findall(pattern, html)
        # print(details)
        detailList = []
        for detail in details:
            # print(detail[0], detail[1], detail[2], detail[3])  # 分别对应作者 内容 配图 点赞数
            haveImg = re.search("img", detail[2])
            if not haveImg:
                # print(detail[0], detail[1], detail[3])
                detailList.append([detail[0].strip(), detail[1].strip(), detail[3].strip()])
        return detailList

    # 加载并提取页面的内容，加入到列表中

    def get_load_page(self):
        # 如果当前未看的页数少于2页，则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                # 获取新一页
                detailList = self.get_duanzi(self.pageIndex)
                # 将该页的段子存放到全局list中
                if detailList:
                    self.stories.append(detailList)
                    # 获取完之后页码索引加一，表示下次读取下一页
                    self.pageIndex += 1

    # 调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self, detailList, page):
        # 遍历一页的段子
        for story in detailList:
            # 等待用户输入
            receive = input()
            # 每当输入回车一次，判断一下是否要加载新页面
            self.get_load_page()
            # 如果输入Q则程序结束
            if receive == "Q" or receive == "q":
                self.enable = False
                return
            print(u"当前第:%s页\n发布人:%s\n内容:%s\n点赞数:%s\n" % (page, story[0], story[1], story[2]))

    def start(self):
        print(u"正在读取糗事百科,按回车查看新段子，Q退出")
        # 使变量为True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        self.get_load_page()
        # 当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                # 从全局list中获取一页的段子
                detailList = self.stories[0]
                # 当前读到的页数加一
                nowPage += 1
                # 将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                # 输出该页的段子
                self.getOneStory(detailList, nowPage)


if __name__ == "__main__":
    spider = QSBK()
    spider.start()
