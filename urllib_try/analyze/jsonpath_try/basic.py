import json
import jsonpath

# https://blog.csdn.net/luxideyao/article/details/77802389

# 内容
obj = json.load(open('../../res/jsonpath/store.json', 'r', encoding='utf-8'))

# 指定元素获取
author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
authors = jsonpath.jsonpath(obj, '$..author')


print(authors)
