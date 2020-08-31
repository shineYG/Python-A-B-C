# -*- coding: utf-8 -*-

from twilio.rest import Client
# Twilio 注册信息
account_sid = "ACdff1eb1231d6d8760ac20c936777ab76"
auth_token = "4bb47876b3fd147fe6daf42aa5e138ab"

client = Client(account_sid, auth_token)
message = client.messages.create(
    # 中国的号码前面需要加86
    to="+86XXXXXXXXXX",
    from_="+12058803434",
    body="Python Send Message!")

print(message.sid)
