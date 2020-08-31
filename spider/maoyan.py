import json
import requests
from requests.exceptions import RequestException
import re
import time

def get_one_page(url):
    try:
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
'''
<dd>
    <i class="board-index board-index-1">1</i>
    <a href="/films/1375" title="活着" class="image-link" data-act="boarditem-click" data-val="{movieId:1375}">
        <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"
             alt="" class="poster-default">
        <img alt="活着" class="board-img"
             src="https://p0.meituan.net/movie/4c41068ef7608c1d4fbfbe6016e589f7204391.jpg@160w_220h_1e_1c">
    </a>
    <div class="board-item-main">
        <div class="board-item-content">
            <div class="movie-item-info">
                <p class="name"><a href="/films/1375" title="活着" data-act="boarditem-click"
                                   data-val="{movieId:1375}">活着</a></p>
                <p class="star">
                    主演：葛优,巩俐,牛犇（bēn）
                </p>
                <p class="releasetime">上映时间：1994-05-17(法国)</p></div>
            <div class="movie-item-number score-num">
                <p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>
            </div>
        </div>
    </div>
</dd>
'''
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\\d+)</i>.*?data-act="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    print(len(items))
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(content)
        # f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    write_to_file(html)
    # for item in parse_one_page(html):
    #     write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)