# coding = utf-8

# 输入圆的半径，计算圆的面积

import math
import re

str = input("请输入圆的半径:")
while not re.findall('^[0-9|.]+$', str): # 限制输入的必须是数字
    str = input("输入的参数必须为数字:")

r = float(str)
# area = round(math.pi * r * r, 2) # 保留2位小数
area = round(math.pi * pow(r, 2), 2) # 保留2位小数
print(area)

