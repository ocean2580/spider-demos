import urllib.request
import urllib.parse

url = "https://www.baidu.com/s?wd="
name = urllib.parse.quote('周冬雨')    # 转 Unicode
url += name
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",

}

# 请求对象定制，解决反爬
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('UTF-8')

print(content)