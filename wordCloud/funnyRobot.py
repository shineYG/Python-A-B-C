from tkinter import *
import time
import requests
from bs4 import BeautifulSoup
import bs4
import random
import re


# 根据url抓取页面信息
def get_html_text(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.text
    except:
        print('fail to getHMTLText...')
        return ''


def fill_univ_list(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find_all('code'):
        ulist.append(tr.string)


def print_univ_list(ulist, k):
    return ulist[k]


# 段子
def get_duanzi():
    uinfo = []
    u = 'http://duanziwang.com/category/%E4%B8%80%E5%8F%A5%E8%AF%9D%E6%AE%B5%E5%AD%90/'
    i = random.randint(1, 100)
    url = u + str(i) + '/'
    html = get_html_text(url)
    fill_univ_list(uinfo, html)
    k = random.randint(1, len(uinfo)-1)
    return print_univ_list(uinfo, k)


def fill_joke(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find_all('div', 'article block untagged mb15 typs_hot'):
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find('div', 'content')
            tdss = tds('span')
            reg = re.compile('<[^>]*>')
            text = reg.sub('', str(tdss))
            regg = re.compile('\\[|\\]|\\n')
            text = regg.sub('', text)
            ulist.append(text)


# 笑话
def get_joke():
    ulist = []
    u = 'https://www.qiushibaike.com/text/page/'
    i = random.randint(1, 13)
    url = u + str(i) + '/'
    html = get_html_text(url)
    fill_joke(ulist, html)
    k = random.randint(0, len(ulist)-1)
    return str(ulist[k])


if __name__ == '__main__':
    # duanzi = get_duanzi()
    # print(duanzi.strip())
    print(get_joke())