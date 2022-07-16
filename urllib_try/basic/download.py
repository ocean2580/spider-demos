import urllib.request

# html
url_page = "http://www.baidu.com"
urllib.request.urlretrieve(url_page, '../res/baidu.html')

# img
url_img = "https://img0.baidu.com/it/u=775547737,2915979378&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=304"
urllib.request.urlretrieve(url_img,'../res/girl.jpg')

# video
url_video = "https://vd4.bdstatic.com/mda-ketdpvyatbf5c4kg/v1-cae/sc/mda-ketdpvyatbf5c4kg.mp4?v_from_s=hkapp-haokan-nanjing&amp;auth_key=1657854801-0-0-de2a8d21fe826932f632bc9e2edde439&amp;bcevod_channel=searchbox_feed&amp;pd=1&amp;cd=0&amp;pt=3&amp;logid=2601023370&amp;vid=10456156410676706005&amp;abtest=103525_2&amp;klogid=2601023370"
urllib.request.urlretrieve(url_video,'../res/h.mp4')
