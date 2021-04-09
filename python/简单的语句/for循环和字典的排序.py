# 取出字典的key-value
dt = {'name':'ABC', 'age':20, 'city': 'shenzhen'}

# 第一种方法
for k in dt:
    print(k, dt[k])

# 第二种方法
for k,v in dt.items():
    print(k,v)   
    