# coding=utf-8

'''
    爬取http://www.itdiffer.com/books.html这个网页中所显示书籍名
'''

import requests
from lxml import etree

url = "http://www.itdiffer.com/books.html" # 跟老奇学Python
req = requests.get(url)
status_code = req.status_code
print('status_code:',status_code)

req.encoding = 'utf-8'  #网页解码方式
html = req.text         #获取网页源码 用html变量接收 text或content

selector = etree.HTML(html)
#infors = selector.xpath('//div[@id="menu"]/div[@class="contain"]/ul/li/a') #提取菜单栏url
content = selector.xpath('//ul[@class="articles"]/li/a/text()') # 根据html标签过滤内容

result =[str(i).replace('\n','').replace(' ','') for i in content]
print(result)