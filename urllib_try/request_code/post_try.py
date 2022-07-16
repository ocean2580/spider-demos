import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}

data = {
    'kw': 'cat'
}
data = urllib.parse.urlencode(data).encode('UTF-8')  # post请求内容转码

request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
obj = json.loads(content)
print(obj)