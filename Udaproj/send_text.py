# -*- coding:utf-8 -*-
from twilio.rest import Client
'''

需要注册
从https://www.twilio.com/console上获取你的ACCOUNT SID, AUTH TOKEN
官方文档中查看,API已更新

'''
account_sid = "AC604e0095faac36138d68e8175aa7d6d8"
auth_token = "59f8d3b62a193d1dec801c941bea3ee4"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello,World",  # SMS正文
    to="+8615855834240",  # Phone Number
    from_="+12608888237 " ,  # Twilio Number
    media_url="http://www.codedraw.cn/wp-content/uploads/2017/10/Blue_Beau.jpg"
    # 查看官方文档会发现也可以发送媒体文件
)
print (message.sid)