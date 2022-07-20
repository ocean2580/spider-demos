import urllib.request
import urllib.parse
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1658283443169_63&jsoncallback=jsonp64&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1658283443169_63&jsoncallback=jsonp64&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
    'cache-control': 'no-cache',
    'cookie': 'miid=4932303601862955207; cna=waceGtxWPVcCAX1Wo3yPQKg6; t=733e0e785f46ea3fbbb5af037288b952; thw=cn; cookie2=16004f1f9233377fd7f3a6c7b7441222; v=0; _tb_token_=e773033b6687e; xlly_s=1; _m_h5_tk=a5cf630e4b1cc2871acfd759f1e69b9d_1658292348165; _m_h5_tk_enc=d5fd90ae77309ea63975ceaef459f164; hng=GLOBAL%7Czh-CN%7CUSD%7C999; _uetsid=095397a007d211eda4f359f2838f0d21; _uetvid=095431e007d211ed85f553e01d18bffb; _ga=GA1.2.1277894565.1658283420; _gid=GA1.2.1220899976.1658283421; _gat_gtag_UA_202630127_1=1; _ga_YFVFB9JLVB=GS1.1.1658283420.1.0.1658283422.0; tfstk=cWrdBJjlK1fnSJujPJQizMVm5vBGZ_JKZpGJ2uzb5mHAs7xRi1r0DuflRYlq9OC..; l=eBjuvZwqg8ZGUcwwBOfahurza779KIRbGuPzaNbMiOCPOh1pU-G5W6vlu289CnhVn6opR3Wrj_IwBlT3NyUC5g9vK_cZo_3_FdTh.; isg=BGtrPx-MjWWMd9KBXOhfvM6l-o9VgH8CEikwP93oBaoffIreZVEZUqrS17wSpNf6',
    'pragma': 'no-cache',
    'referer': 'https://www.taobao.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# 得到 json数据
content = content.split('(')[1].split(')')[0]

with open('../../res/jsonpath/ticket.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

# jsonpath操作
obj = json.load(open('../../res/jsonpath/ticket.json', 'r', encoding='utf-8'))
region_list = jsonpath.jsonpath(obj, '$..regionName')
print(region_list)