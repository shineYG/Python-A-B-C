import smtplib
from email.mime.text import MIMEText

def send_mail(sender, password, receivers, title, content):
    msg = MIMEText(content)
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = ';'.join(receivers)

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        return True
    except:
        return False

if __name__ == '__main__':
    sender = 'xxxxxxxxxx@qq.com'
    password = 'xxxxxxxxx'
    receivers = ['xxxxx@163.com', 'xxxxxx@qq.com']
    title = '邮件群发'
    content = '这是一份群发的测试邮件'
    if send_mail(sender, password, receivers, title, content):
        print('群发成功！ ')
    else:
        print('群发失败！ ')

