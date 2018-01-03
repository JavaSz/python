# -*- coding:utf-8 -*-
import time
import pygame
import webbrowser


file=r'F:\Siji.mp3'
pygame.mixer.init()
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.music.stop()

time_break = 24
time_begin = 0
while(time_break > time_begin):  # 循环24次
    time.sleep(10)    # time.sleep(secs)从而暂停10秒
    webbrowser.open('www.baidu.com')  # 10秒后启动浏览器
    time_begin = time_begin + 1
