import urllib.request
url = 'https://qzone.qq.com/'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

with open('../res/qq/qqZone.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
