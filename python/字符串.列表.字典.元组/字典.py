# encoding=utf-8
# 字典，必须要用 {}，由键值对组成，键值对的Key不能重复
# 第一种定义方式
a = {'name':'ABC', 'age':20, 'city': 'shenzhen'}
print('a=>', a)

# 第er种定义方式
b = dict(name = 'ABC', age = 20, city = 'shenzhen')
print('b=>', b)
c = dict([('name', 'ABC'), ('age', 20), ('city', 'shenzhen')])
print('c=>', c)

# 获取键值对的值，这个是否name必须要在字典中
print("a['name']=>", a['name'])
# 使用get，不在字典中会返回None
print("a.get('name')=>", a.get('na'))
# 使用get，不在字典中则设置默认值
print("a.get('nam')=>", a.get('nam', '111111111'))

print("a.setdefault('na')=>",a.setdefault('na'))
print(a)
print("a.setdefault('nam', '111111111')=>", a.setdefault('nam', '111111111'))
print(a)

# 获取字典的长度
print('=>len(a)', len(a))

# 修改字典中某个键的值
a['name'] = 'test'
print('a=>', a)

# 删除字典中指定地键值对，用 del 函数
del a['name']
print("del a['name']=>", a)
# 删除字典中指定地键值对，用 pop 函数
a.pop('na')
print("a.pop('na')=>", a)
# 从字典a中删除键na，如果存在就直接删除，如果不存在，则返回给的默认是not exist
a.pop('na','not exist')
print(a)
# 删除字典中的最后一个键值对
a.popitem()
print('a.popitem()=>',a)


# 判断键是否在字典中
if  'name' in a:
    print('true')
else:
    print('false')

# 向字典中插入键值对方法一：插入元组
a.update([('sex', 0), (('job', 'develper'))])
print(a)

# 向字典中插入键值对方法一：将另外一个字典追加到字典后面
b = {'color':'green', 'price':3.14}
a.update(b)
print(a)



