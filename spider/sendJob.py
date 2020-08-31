import requests
from bs4 import BeautifulSoup
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import logging
import smtplib
import schedule

def get_weather():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    resp = requests.get('http://www.weather.com.cn/weather/101190101.shtml', headers = headers)
    resp.encoding='utf-8'
    bs = BeautifulSoup(resp.text, 'html.parser')
    date = bs.find('h1').text
    weather = bs.find('p', class_='wea').text
    temperature = bs.find('p', class_='tem').text.replace('\n', '').replace('\r', '')
    return date, weather, temperature

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def sendmail(to_addr, weather_info):
    from_addr = 'yangguang914@163.com'
    password = 'NDNQSJRPIDWSCHNQ'
    smtp_server = 'smtp.163.com'

    #发送地址格式 都需要编码
    msg = MIMEText(weather_info)
    msg['Subject'] = '天气预报'
    msg['From'] = from_addr
    msg['To'] = to_addr
    
    try:
        server = smtplib.SMTP_SSL(smtp_server, 465)  # 启用SSL发信, 端口一般是465
        server.login(from_addr, password)
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPException as e:
        logging.error('sendemail:%s'%e)

def job(msg):
    sendmail('513981883@qq.com', msg)
    print('天气预报发送成功！')

date, weather, temperature = get_weather()
msg = '今天：{}，天气：{}， 温度：{}'.format(date, weather, temperature)
schedule.every(10).seconds.do(job, msg)

while True:
    schedule.run_pending()
