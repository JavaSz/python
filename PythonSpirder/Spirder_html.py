# -*- coding: UTF-8 -*-
import io
import sys
import urllib.request
import urllib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 改变标准输出的默认编码
res = urllib.request.urlopen('https://www.codedraw.cn')
htmlBytes = res.read()
print(htmlBytes.decode('utf-8'))

