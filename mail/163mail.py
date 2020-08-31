from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import logging
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'xxxxxxxxxxxxx@163.com'
password = 'xxxxxxxxxxxx'


# 输入SMTP服务器地址:
smtp_server = 'smtp.163.com'

def sendmail(to_addr,link,secure=True):
    title = '<html><body><h3>亲爱的<a data-auto-link="1" href="mailto:%s" target="_blank">%s</a>,您好:</h3>'%(to_addr,to_addr)
    reset = "<div style = 'padding-left:55px;padding-right:55px;font-family:'微软雅黑','黑体',arial;font-size:14px;'>重置密码</div>"
    body = '<p>请点击以下链接进行重置密码 <a href="%s">%s</a></p>'%(link,reset)
    tail = '如果您并不是Awesome用户，可能是其他用户误输入了您的邮箱地址。</body></html>'
    html = title+body+tail
    msg = MIMEText(html, 'html', 'utf-8')
    #发送地址格式 都需要编码
    msg['From'] = _format_addr('Awesome Python Webapp <%s>' % from_addr)
    msg['To'] = _format_addr('亲爱的用户 <%s>' % to_addr)
    msg['Subject'] = Header('重置密码', 'utf-8').encode()
    
    try:
        server = smtplib.SMTP_SSL(smtp_server, 465)  # 启用SSL发信, 端口一般是465
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
    except smtplib.SMTPException as e:
        logging.error('sendemail:%s'%e)

if __name__ == '__main__':
    # 输入收件人地址:
    to_addr = 'xxxxxxxxxx@qq.com'
    sendmail(to_addr,'http://www.baidu.com',True)