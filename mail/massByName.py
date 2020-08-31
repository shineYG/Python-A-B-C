import smtplib
from string import Template
from email.mime.text import MIMEText

# 读取自定义邮件模版
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        return Template(template_file.read())

# 获取收件人信息，格式：xx xx@qq.com
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contact_file:
        for contact in contact_file:
            names.append(contact.split()[0])
            emails.append(contact.split()[1])
    return names, emails

# 登录邮箱
server = smtplib.SMTP_SSL('smtp.qq.com', 465)
server.login('xxxxxxxxx@qq.com', 'xxxxxxxx')

# 获取邮件模版
template = read_template('content.txt')
names, emails = get_contacts('contacts.txt')
for name, email in zip(names, emails):
    # 渲染模版，生成邮件内容
    content = template.safe_substitute(person=name)
    msg = MIMEText(content)
    msg['Subject'] = '邮件群发'
    msg['From'] = 'xxxxxxxxx@qq.com'
    msg['To'] = email
    server.send_message(msg)

    del msg

# 退出登录
server.quit()