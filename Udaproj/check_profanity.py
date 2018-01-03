# -*-coding:utf-8 -*-
'''
编写一个程序
可以读取电脑中的某个txt文件
并检测其中内容是否包含不礼貌的用语
'''

# 首先我们应该定义一个函数可以读取txt文件
import urllib

def read_txt():
    open_txt = open("F:\movie_quotes.txt")
    read_content = open_txt.read()
    print(read_content)
    open_txt.close()
    check_profanity(read_content)
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot" + text_to_check)  # 在线冒犯用语检测
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This is Document has not curse words!")
    else:
        print("Can Not Scan The Document Properly")
read_txt()
