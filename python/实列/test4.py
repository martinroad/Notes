'''
创建一个数据集，包含1到10的随机整数，共计100个，然后统计每个数字出现的次数
'''

import random

# 方法1：
lst = []
i = 0
while i < 100:
   number = random.randint(1,10)
   lst.append(number)
   i += 1

#  方法2：
# for i in range(100):
#     number = random.randint(1,10)
#     lst.append(number)

d = {}
for n in lst:
    if n in d:
        d[n] += 1
    else :
        d[n] = 1

# 得到结果
print(d)

# 将结果按照key升序排列
print(sorted(d.items()))
# 将结果按照key升序排雷，并将列表转换成字典
print(dict(sorted(d.items())))

# key使用lambda匿名函数取value进行升序排序，并将列表转换成字典
print(dict(sorted(d.items(), key= lambda item:item[1])))

# key使用lambda匿名函数取value进行降序排序，并将列表转换成字典
print(dict(sorted(d.items(), key= lambda item:item[1], reverse=True)))