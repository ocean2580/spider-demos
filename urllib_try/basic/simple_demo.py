import urllib.request

# 1.target url
# https 会遭到 反爬
url = 'http://www.baidu.com'

# 2.request
# 返回类型 HttpResponse
response = urllib.request.urlopen(url)

# 3.analyze
# read 默认二进制字节码
content = response.read().decode('UTF-8')

# 4.use
print(content)
