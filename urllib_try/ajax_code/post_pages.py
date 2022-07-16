import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        'cname': '',
        'pid': '',
        'keyword': '江西',
        'pageIndex': page,
        'pageSize': '10'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    }
    request = urllib.request.Request(url=base_url, headers=headers,data=data)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page, content):
    with open('../res/kfc/kfc_' + str(page) + '.json','w', encoding='utf-8') as fp:
        fp.write(content)


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
        down_load(page, content)
