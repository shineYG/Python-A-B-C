import requests

# resp = requests.get('https://github.com/favicon.ico')
# with open('github.ico', 'wb') as file:
#     file.write(resp.content)

# 添加headers并加上User-Agent信息，才能正常爬取
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# print(r.text)

# 文件上传
files = {'file': open('github.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)