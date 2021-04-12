
# //! 几个常用于for循环的函数：
# //! 1、range() 函数：是一个迭代器对象
for i in range(10):
    print(i)

# 得到列表
print(list(range(10))) #结果为 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 得到列表，步长为2
print(list(range(0, 10, 2))) #结果为 [0, 2, 4, 6, 8]


# //!2、zip() 函数：将两个列表中的元素配对，组合成新的元素，以短的为主
a = [1,2,3,4,5]
b = [6,7,8,9]
print(list(zip(a,b))) #结果为 [(1, 6), (2, 7), (3, 8), (4, 9)]

# //!示例
# 有两个列表 c = [1, 2, 3, 4, 5], d = [5, 6, 7, 8, 9]，现要求将列表c和列表d对应的元素相加，得到新的列表：[6,8,10,12,14]
# //todo方法一：
c = [1, 2, 3, 4, 5]
d = [5, 6, 7, 8, 9]
result = []
for i in range(len(c)):
    result.append(c[i]+d[i])
print(result)    #结果为[6, 8, 10, 12, 14]

# //todo方法二：
result =[]
e = list(zip(c,d))
print(e)         #结果为[(1, 5), (2, 6), (3, 7), (4, 8), (5, 9)]
for x,y in e:
    result.append(x+y);
print(result)    #结果为[6, 8, 10, 12, 14]


# //!3、enumerate() 枚举函数:
f = ['one', 'two', 'three', 'four']
print(list(enumerate(f))) #结果为 [(0, 'one'), (1, 'two'), (2, 'three'), (3, 'four')]，前面的 0，1，2，3是索引

# //!示例：
# //todo方法一：
# 已知列表 g = [1, 5, 3, 20, 6, 2, 7]，将偶数替换为 'even'
g = [1, 5, 3, 20, 6, 2, 7]
for i in range(len(g)):
    if g[i] % 2 == 0:
        g[i] = 'even'
print(g)    #结果为[1, 5, 3, 'even', 'even', 'even', 7]

# //todo方法二：
g = [1, 5, 3, 20, 6, 2, 7]
for i,ele in enumerate(g):
    if ele % 2 == 0:
        g[i] = 'even'
print(g)      #结果为[1, 5, 3, 'even', 'even', 'even', 7]