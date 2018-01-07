# @File  : TBMM.py
# @Author: Zhang
# @Date  : 2018/1/7
# @Contact : codecool97@gmail.com 
# @Desc  : https://www.codedraw.cn
import requests
import re
import os
import time


class MMSpider:
    def __init__(self):
        self.base_url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
        self.headers = {'user-agent':
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
                        }
        self.base_path = r"F:\TaoBaoMM"
        # MM个人主页
        self.base_person_url = "http://mm.taobao.com/self/aiShow.htm?userId="
        # MM相册主页
        self.person_album_url = 'https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20='
        # MM图片具体地址
        self.base_pic_url = 'https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id='
        self.__page = 1
        self.current_page = 1
        self.album_pattern = re.compile('''<h4>.*?album_id=(.*?)&''', re.S)
        self.album_page_pattern = re.compile('''<input name="totalPage" id="J_Totalpage" value="(.*?)"''', re.S)


    # 得到json中数据
    def get_person_dict(self, currentPage):
        try:
            url = self.base_url + str(currentPage)
            r = requests.get(url).json()
            return r
        except Exception as e:
            return e

    def save(self, searchList):
        # 进入每个模特的主页，找到相册地址
        # 保存对每个模特创建一个文件夹，保存文字信息并进入相册下载图片
        for person in searchList:
            # 创建文件夹，realName中是MM的姓名，保存信息
            dir_path = self.base_path + "\\" + person["realName"]
            if self.mkdir(dir_path):
                txt_path = dir_path + "\\" + person["realName"] + ".txt"
                # MM信息.txt
                self.write_txt(txt_path, person)
                self.save_images(person, dir_path)

    def write_txt(self, txt_path, person):
        # 拼接MM主页URL
        person_url = self.base_person_url + str(person["userId"])
        content = "姓名:" + person["realName"] \
                  + "\n城市:" + person["city"] \
                  + "\n身高:" + str(person["height"]) + "cm" \
                  + "\n体重:" + str(person["weight"]) + "kg" \
                  + "\n辣么多人喜欢她:" + str(person["totalFavorNum"]) + "人" \
                  + "\n个人主页:" + person_url
        with open(txt_path, "w", encoding="utf-8") as file:
            print("正在保存: " + person["realName"] + "的文字信息")
            file.write(content)
            print("文字信息保存完毕")

    def save_images(self, person, dir_path):
        # 找到MM的相册一共有多少页
        album_page = self.get_album_page(person["userId"])
        print()
        album_index = 1
        # 在每一页中操作找到该页中album的id
        for i in range(1, int(album_page) + 1):
            album_ids = self.get_album_ids(person["userId"], i)
            for album_id in album_ids:
                pic_page = self.get_pic_page(person["userId"], album_id)
                # 将每一页的图片保存下来
                for j in range(1, int(pic_page) + 1):
                    imgs_url = self.get_imgs_url(person, j, album_id)
                    for img_url in imgs_url:
                        try:
                            url = "http:" + img_url["picUrl"]
                            r = requests.get(url)
                            with open(dir_path + "\\" + str(album_index) + ".jpg", "wb") as file:
                                file.write(r.content)
                                if album_index % 100 == 0:
                                    print("...休息一下")
                                    time.sleep(1)
                                if album_index >= 500:
                                    print(person["realName"] + ":已经保存500张辣,换一个MM吧")
                                    return
                                album_index = album_index + 1
                        except Exception as e:
                            return e

    # 创建文件夹 判断文件夹是否存在
    def mkdir(self, dir_path):
        if os.path.exists(dir_path):
            return False
        else:
            os.mkdir(dir_path)
            return True

    # 获得用户ID
    def get_album_ids(self, userId, page):
        try:
            # 相册信息
            all_album_url = self.person_album_url + str(userId) + "&" + str(page)
            r = requests.get(all_album_url).text
            # 提取该页中album的id
            return re.findall(self.album_pattern, r)
        except Exception as e:
            print("提取相册id出错...错误:", e)

    # 获得MM相册页数
    def get_album_page(self, userId):
        try:
            url = self.person_album_url + str(userId)
            r = requests.get(url)
            # print(r.encoding)
            # print(r.text)
            return re.search(self.album_page_pattern, r.text).group(1)
        except Exception as e:
            return "获取相册页面数量发生错误", e

    # 找到图片地址
    def get_imgs_url(self, person, j, album_id):
        url = self.base_pic_url + str(person["userId"]) \
              + "&album_id=" + str(album_id) \
              + "&page=" + str(j)
        try:
            r = requests.get(url, timeout=30)
            imgs_url = r.json()["picList"]
            return imgs_url
        except Exception as e:
            return e

    def get_pic_page(self, userId, albumId):
        try:
            # 先得到这个相册一共有多少页
            url = self.base_pic_url + str(userId) + "&album_id=" + str(albumId)
            r = requests.get(url).json()
            return r["totalPage"]
        except Exception as e:
            return e

    def start(self):
        print("开始爬取MM")
        for i in range(self.__page):
            dict_result = self.get_person_dict(self.current_page)
            # json文件中的searchDOList保存着MM信息
            searchList = dict_result["data"]["searchDOList"]
            # print(searchList)
            # 保存所有本页中MM的信息
            self.save(searchList)
            self.current_page += 1


if __name__ == "__main__":
    spider = MMSpider()
    spider.start()
