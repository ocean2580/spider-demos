import urllib.request
from lxml import etree

url = 'http://www.baidu.com'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

tree = etree.HTML(content)
# 返回类型 list
result = tree.xpath('//input[@id="su"]/@value')

print(result[0])
