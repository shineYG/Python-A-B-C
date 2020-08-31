# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp = "smtp.qq.com"

sender = 'xxxxxxx@qq.com'
receiver = 'xxxxxxxxx@163.com'
# 授权密码
pwd = 'xxxxxxxxxxx'

title = "hello I am Python"
contents = "{}发送给{}的邮件".format(sender, receiver)


try:
    ldqplxo = MIMEText(contents, 'plain', 'utf-8')
    ldqplxo['From'] = Header(sender, 'utf-8')
    ldqplxo['To'] = Header(receiver, 'utf-8')
    ldqplxo['Subject'] = Header(title, 'utf-8')
    mbdrewr = smtplib.SMTP_SSL(smtp, 465)
    mbdrewr.login(sender, pwd)
    mbdrewr.sendmail(sender, receiver, ldqplxo.as_string())
    mbdrewr.quit()
except Exception as e:
    print('错误>>>', e)