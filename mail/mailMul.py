import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
 
fromAddr = 'xxxxxxxxxxxxx@163.com'
password = 'xxxxx'
toAddr = 'xxxxxx@qq.com'

# 附件添加内容
message = MIMEMultipart()
message['Subject'] = "Python Test"
message['From'] = fromAddr
message['To'] = toAddr
#邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
 
# 附件上传文本
att1 = MIMEText(open('C:\\Users\\shine\\Desktop\\test1.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test1.txt"'
message.attach(att1)
 
# 附件上传图片
with open('C:\\Users\\shine\\Desktop\\sunset.jpg', 'rb') as fp:
	img = MIMEImage(fp.read())
img["Content-Disposition"] = 'attachment; filename="sunset.jpg"'
message.attach(img)



# 输入SMTP服务器地址:
smtp_server = 'smtp.163.com'
try:
    server = smtplib.SMTP_SSL(smtp_server, 465)  # 启用SSL发信, 端口一般是465
    server.login(fromAddr, password)
    server.send_message(message)
    server.quit()
except smtplib.SMTPException as e:
    logging.error('sendemail:%s'%e)