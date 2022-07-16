import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}

request = urllib.request.Request(url=url, headers=headers)

# 代理
proxies = {
    # 'ip: port'
    'http': '103.170.27.237:80',
}

# ProxyHandler()
handler = urllib.request.ProxyHandler(proxies=proxies)  # 添加代理池
opener = urllib.request.build_opener(handler)
response = opener.open(request)


content = response.read().decode('utf-8')

print(content)
