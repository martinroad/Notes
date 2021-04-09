# coding=utf-8
# coding:utf-8

import decimal
from typing import ByteString

a = 3.14
print(type(a)) 
print(id(a))

b= decimal.Decimal('0.12')
c = 0.12
print(b)
print(c)

d = 2**10
print('2**10=>', d)

# 字符串可以用单引号或者双引号，但是有单引号的情况下，最外层必须要用双引号
e = "what's your favorite "
print(e)
print(e*3)

# 判断字符是否在字符串中
f = "pythonpp python"
if  'p' in f:
    print("True")
else:
    print ("False")

# string.index() 函数
print("f.index('p',3,10)=>", f.index('p',3,10)) # 取f字符串中第3号位到第19号位置之间的， 字符'p'第一次出现的索引

# 字符串切片
f = 'python book'
print(f[0]) # 取第一个字符（0号位置）
print(f[3:7]) # 取3号位置到7号位置（不包含7号位）的字符，步长默认为1，可以不写
print(f[3:7:1]) # 取3号位置到7号位置的，步长为1
print(f[0:7:1]) # 取0号位置到7号位置的，步长为1
print(f[:7:1]) # 取0号位置到7号位置的，步长为1
print(f[2:]) # 从第二个字符开始，到字符串的结尾，步长为1
print(f[:]) # 从第0个字符开始，到字符串的结尾，步长为1

print(f[::-1]) # 字符串反序了，得到'koob nohtyp'，从右边到左边，索引依次是-1,-2,-3,-4 ...


# 字符串的拆分，拼接
g = "I LOVE PYTHON"
g = g.split(' ')
print(g)
g = "-".join(g)
print(g)


# 字符串的fromat格式化
h = "My name is %s and weight is %d kg!" % ('Zara', 21)
print(h) 
h = "i love {0} and {1}".format("java", "python")
print(h)

# 第一个参数要有10个字符长度，第2个参数要有15个字符长度，并且第二个参数要右对齐
h = "I like {0:10} and {1:>15}".format("java", "python")
print(h)
# 第一个参数要有10个字符长度，并且第一个参数要居中，第2个参数要有15个字符长度，并且第二个参数要左对齐
h = "I like {0:^10} and {1:<15}".format("java", "python")
print(h)
# 第一个参数要有3个字符长度，并且第一个参数是int类型，整数默认是右对齐，第2个参数是float类型，并且第二个参数保留一位小数，默认是四舍五入
h = "she is {0:3d} years old and {1:0.1f}".format(28, 1.68)
print(h)




