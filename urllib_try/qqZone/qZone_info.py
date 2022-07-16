import urllib.request
import gzip
from io import BytesIO
# 直接访问个人信息页面会被拦截，跳转到登录界面（非 utf-8 编码）

headers = {
    # ':authority': 'user.qzone.qq.com',
    # ':method': 'GET',
    # ':path': '/2080917477',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
    'cache-control': 'no-cache',
    # cookie 登录携带
    'cookie': 'RK=drAJuKtqMW; ptcz=09fa6dfb9b993b798e1ed78729940f776d5129ce3037b2b33153c32cb643869d; pgv_pvid=2908676027; tvfe_boss_uuid=f3b6fae1b0d1834a; fqm_pvqid=a0384177-b846-49a4-ba14-31b1690a5e1d; QZ_FE_WEBP_SUPPORT=1; pac_uid=0_ca52e49117e7a; eas_sid=z1f6y5s5i9G5R4K8T1E0W97661; Loading=Yes; qz_screen=1536x864; __Q_w_s__QZN_TodoMsgCnt=1; cpu_performance_v8=49; _qpsvr_localtk=0.16648355259962289; pgv_info=ssid=s1034404490; uin=o2080917477; skey=@xK6ptlKYU; p_uin=o2080917477; pt4_token=8G4GxMEENhnsXDC0KdZEIfNF3qmW3P2nCpRrhMihkfk_; p_skey=vSudZQVIP6TdEfkZ370RnLikhXVS*VqF*bA6LfYJ1ZU_; 2080917477_todaycount=0; 2080917477_totalcount=8364',
    'pragma': 'no-cache',
    # refer 防盗链
    'referer': 'https://qzs.qq.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',}

url = 'https://user.qzone.qq.com/2080917477'
request = urllib.request.Request(url=url, headers=headers)

# 2.响应请求
response = urllib.request.urlopen(request)
html = response.read()
buff = BytesIO(html)
f = gzip.GzipFile(fileobj=buff)
content = f.read().decode('UTF-8')

# 3.保存数据
with open('../res/qq/qqZoneInfo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)




