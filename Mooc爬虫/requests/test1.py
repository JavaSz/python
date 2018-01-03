import requests

import time



def getHtml(url):

    try:

        r=requests.get(url, timeout=10)

        r.raise_for_status

        return 'ok'

    except:

        return'失败'



url='http://220.178.71.156:85/(ndsb4255vl13veqlvdimc255)/default2.aspx'

t1=time.time()  # 获取当前的时间

try:

    for i in range(1):

        getHtml(url)

    t2 = time.time()  # 爬取100次之后的时间
    duration = t2 - t1
    print(duration)  # 耗时

    print("爬取成功 用时:"+duration+'s')

except:

    print("爬取失败")