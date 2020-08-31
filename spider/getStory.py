import requests
from bs4 import BeautifulSoup
import openpyxl

# 爬取网站html信息
rep = requests.get('https://www.lingdianshuwu.com/')
rep.encoding='gb2312'

# 解析网页内容
bs = BeautifulSoup(rep.text, 'html.parser')
li_tags = bs.find_all('li', class_='new_2')

story_list = [['名字', '链接']]

# 遍历节点内容
for content in li_tags:
    a = content.find('a')['href']
    story_list.append([content.text, 'https://www.lingdianshuwu.com/' + a])

# 写入excel
wb = openpyxl.Workbook()

# 创建活动页
sheet = wb.active
sheet.title = '我的小说'

# 写入操作
for story in story_list:
   sheet.append(story) 

# 保存excel
wb.save('myStory.xlsx')    

