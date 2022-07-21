from selenium import webdriver

# 模拟浏览器行为, js操作
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = "http://www.bilibili.com"
browser.get(url)
browser.close()
