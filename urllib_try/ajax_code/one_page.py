import urllib.request

# 1.定制对象
url = 'https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start=0&limit=20'
headers = {
    # user-agent
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}
request = urllib.request.Request(url=url, headers=headers)

# 2.响应请求
response = urllib.request.urlopen(request)
content = response.read().decode('UTF-8')

# 3.保存数据
with open('../res/db.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
