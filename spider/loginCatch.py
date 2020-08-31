import requests
from bs4 import BeautifulSoup

# 登录
def login():
    data = {"username":"shine","password":"shine19870914","action":"login"}
    resp = requests.post('https://www.xslou.com/login.php', data=data)
    resp.encoding='gb2312'
    return resp.cookies

# 榜单
def top_list():
    books = {}
    resp = requests.get('https://www.xslou.com/top/allvisit_1/', timeout=10)
    try:
        resp.raise_for_status()
    except:
        print('get top list timeout! ')
    resp.encoding='gb2312'
    bs = BeautifulSoup(resp.text, 'html.parser')
    spanTags = bs.find_all('span', class_='up2')
    for tag in spanTags:
        url = tag.find('a')['href']
        bookId = ''.join(filter(str.isdigit, url))
        books[bookId] = tag.text
    return books

# 推荐
def recommend(book_id):
    resp = requests.get('https://www.xslou.com/modules/article/uservote.php?id=' + book_id, cookies=login())
    resp.encoding = 'gb2312'
    bs = BeautifulSoup(resp.text, 'html.parser')
    title = bs.find('div', class_='blocktitle').text
    content = bs.find('div', class_='blockcontent').find('div').text
    print('推荐结果：{}。推荐信息：{} '.format(title, content))

if __name__ == '__main__':
    for id, name in top_list().items():
        print('{:5} : {}'.format(id, name))
    book_id = input('请输入需要推荐的书籍编号： ')
    recommend(book_id)