import requests
import os
import time
from bs4 import BeautifulSoup
from lxml import etree
# 爬取喜马拉雅FM的热门歌曲到本地

# 模拟浏览器请求
headers = {'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        }


def get_detail_url():
    page_urls = ['http://www.ximalaya.com/dq/{}/'.format(pagenum) for pagenum in range(1, 85)]
    # 热门页面总共84页 获取每个页面的url 是一个list
    # print(page_urls)
    for page_url in page_urls:
        r = requests.get(page_url, headers=headers)
        # print(r.text)
        demo = r.text
        soup = BeautifulSoup(demo, 'lxml')
        for item in soup.find_all('div', class_='albumfaceOutter'):  # 获取div标签下class=albumfaceOutter的所有元素
            # print(item.a)
            # 获取a标签下面的href标签元素
            href = item.a['href']
            title = item.img['alt']
            img_url = item.img['src']
            hrefs = {
                'href': href,
                'title': title,
                'img_url': img_url
            }
            print(u'正在下载 {}... 请稍后 ... '.format(item.img['alt']))  # 状态
            get_audio(href, title)
            # time.sleep(100)  # 限制爬取速度
            break


def get_audio(url, title):
    r = requests.get(url, headers=headers).text
    audio_list = etree.HTML(r).xpath('//div[@class="personal_body"]/@sound_ids')[0].split(',')
    # split 用,将字符串分割成list
    print(title+'   '+u'存在{}个音频文件'.format(len(audio_list)))
    # mkdir(title)
    # os.chdir(r'F:\xmly\\' + title)  # 切换到指定目录
    for audio_id in audio_list:
        json_url = 'http://www.ximalaya.com/tracks/{}.json'.format(audio_id)
        # print(json_url)
        r = requests.get(json_url, headers=headers).json()
        m4a_url = r.get('play_path')
        print(m4a_url)
        # download(m4a_url)


def mkdir(title):
    path = title.strip()  # 移除空格
    # 判断文件夹是否存在
    # print(os.path.join(r'F:\xmly\\', path))  # 拼接路径
    isExist = os.path.exists(os.path.join(r'F:\xmly\\', path))
    if not isExist:
        print(u'创建一个{}文件夹'.format(title))
        # os.makedirs() os.makedirs() 方法用于递归创建目录。
        # 像 mkdir(), 但创建的所有intermediate-level文件夹需要包含子目录。
        os.makedirs((os.path.join(r'F:\xmly\\'), title))
        return True
    else:
        print('{}already exist'.format(title))
        return False

    
def download(url):
    content = requests.get(url).content  # 返回二进制 --图片 音频
    name = url.split('/')[-1]  # 提取/分割之后的倒数第一个元素
    with open(name, 'wb') as file:
        file.write(content)


if __name__ == '__main__':
    get_detail_url()
