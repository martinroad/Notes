# encoding=utf-8
# 元组，必须要用 ()，而列表是用 []，元组也是序列，元组的运算速度比列表更快一些
a = (1, 2, 3, "python", [1,2,3])
print('a=>', a)
#获取第3个元素，结果为python，元素下标从0开始
print('a[3]=>', a[3])  

# 获取元组的长度
print('len(a)=>', len(a))

# 判断某个元素是否在元表中
if 'python' in a:
    print('true')
else:
    print('false')

# 元组的合并
print('a*2=>', a * 2)
a1 = ('hellow', 'world', 100)
print('a + a1=>', a + a1)

#元组反序排列，结果为([1, 2, 3], 'python', 3, 2, 1)，元素下标从0开始
print('a[::-1]=>', a[::-1])

# 创建一个元素的元表，后面要写一个逗号,
b = (1,)
print('b=>', b)

# 元组和列表互换
t = (1, 2, 3, [4, 5], 'a')
# 元组定义好了之后就是固定的，不支持修改
# t[0] = 100
# print(t)

# 如果要修改，可以先将元组转换成列表，对转换后的列表进行修改，然后再将列表转换成元组
lst = list(t)
print('lst=>', lst)
lst[0] = 100
print('lst=>', lst)
t1 = tuple(lst)
print('t1=>', t1)

