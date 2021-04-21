'''
    爬取丁香园https://ncov.dxy.cn/ncovh5/view/pneumonia这个页面的疫情数据
'''

import re
import json
from datetime import datetime
import pandas as pd
import requests

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
# 得到这个网页的所有数据
page = requests.get(url).content.decode("utf-8")

# 使用正则表达式过滤内容
regexp = "<script id=\"getAreaStat\">([^<]+)"
res = re.findall(regexp, page)
# 去掉首尾的一些字符串，得到所需要的字符串切片
data = res[0][27:-11]
# print(res[0][:-1])
# print(data)

# 转换成字典
dicts = json.loads(data)
# print(dicts)

for row in dicts:
    for key in row:
        if key in ['createtTime', 'modifyTime']:
            row[key] = datetime.fromtimestamp(row[key]/1000).strftime('%Y-%m-%d %H:%M:%S') # 将时间戳转换成：年-月-日 时：分：秒

# DataFrame是Python中Pandas库中的一种数据结构，它类似excel，是一种二维表
# DataFrame的单元格可以存放数值、字符串等，这和excel表很像，同时DataFrame可以设置列名columns与行名index
df = pd.DataFrame(dicts)

# 写入csv文件，mode ='a'表示是往后面追加文件
df.to_csv('ncov1.csv', mode='a', encoding='utf_8_sig') 


