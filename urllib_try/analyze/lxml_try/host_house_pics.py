import urllib.request
from lxml import etree
import urllib.parse


def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = "https://sc.chinaz.com/tupian/qinglvtupian_" + str(page) + '.html'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    # 解析
    tree = etree.HTML(content)
    # 主要拿链接
    # alt
    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
    # 懒加载
    src_list = tree.xpath('//div[@id="container"]//a/img/@src')

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'http:' + src
        url = url.replace('\\', '/')
        # 下载
        urllib.request.urlretrieve(url=url, filename='E:/图片集/test/' + name + '.jpg')


#  程序入口
if __name__ == '__main__':
    start_page = int(input('start:'))
    end_page = int(input('end:'))

    for page in range(start_page, end_page + 1):
        # 1.为每页定制对象
        request = create_request(page)
        # 2.获取响应
        content = get_content(request)
        # 3.下载
        down_load(content)
