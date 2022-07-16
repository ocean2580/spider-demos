from lxml import etree
# 单标签也要闭合

# xpath解析 本地文件
tree = etree.parse('../../res/lxml.html')

# 1.路径指定
# '//' 不考虑层次找子孙; '/' 直接子目录
li_1 = tree.xpath('//body/ul/li')  # '//body//li'

# 2.属性指定
# '/text()' 将 对象地址 转为 内容
li_2 = tree.xpath('//ul/li[@id]/text()')    # '//ul/li[@id="naya"]/text()'
li_3 = tree.xpath('//ul/li[@id]/@class')

# 3.模糊查询
li_4 = tree.xpath('//ul/li[contains(@id,"l")]/text()')
li_5 = tree.xpath('//ul/li[starts-with(@id,"o")]/text()')

# 4.逻辑匹配
# '//ul/li[contains(@id,"l") and @class="c"]/text()'
# '//ul/.. | //ul/..'

print(li_5)
print(len(li_5))

