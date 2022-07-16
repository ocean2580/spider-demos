import urllib.request

url = 'http://www.baidu.com'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}

request = urllib.request.Request(url=url, headers=headers)


# 1.handler
handler = urllib.request.HTTPHandler()
# 2.build_opener()
opener = urllib.request.build_opener(handler)
# 3.open()
response = opener.open(request)


content = response.read().decode('utf-8')

print(content)
