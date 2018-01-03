# -*-coding:utf-8 -*-
'''
编写一个程序，实现电脑每运行一小时，自动打开浏览器播放音乐
第一步:让程序暂停1小时
第二步:打开浏览器

'''
import webbrowser  # 引用webbrowser 
import time        # 引用time
time_break = 24
time_begin = 0
while(time_break > time_begin):  # 循环24次
    time.sleep(10)    # time.sleep(secs)从而暂停10秒
    webbrowser.open('http://www.codedraw.cn/%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90%E6%AD%8C%E5%8D%95/')  # 10秒后启动浏览器
    time_begin = time_begin + 1
    print ("Current Time:"+time.ctime())  # 包含了一个ctime方法表示当前的时间 