# 三个特殊函数：lambda(), map(), filter()

# //! lamada（）函数
def add(x, y):
    return x + y

lam = lambda x, y: x + y

print(add(2, 3)) #结果为:5
print(lam(2, 3)) #结果为:5


# //! map（）函数
m = map(lambda x: x + 3, range(10))
lst = list(m) #结果为：[3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(lst)

# //! 示例:
'''
有两个列表 lst1 = [1, 2, 3, 4, 5], lst2 = [2, 3, 4, 5, 6], lst3 = [3, 4, 5, 6, 7]，要求每个索引位置的元素相加得到 [6, 9, 12, 15, 18]  
'''
lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 3, 4, 5, 6]
lst3 = [3, 4, 5, 6, 7]

# //todo 方法1:
lst = []
for i in range(len(lst1)):
    lst.append(lst1[i] + lst2[i] + lst3[i])
print(lst)    

# //todo 方法2:
print('zip(lst1, lst2, lst3):', list(zip(lst1, lst2, lst3))) #结果为:[(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (5, 6, 7)]

lst.clear()
lst = [x + y + z for x, y, z in zip(lst1, lst2, lst3)]   
print(lst) #结果为:[6, 9, 12, 15, 18]

# //todo 方法3:
lst.clear()
lst = list(map(lambda i: lst1[i] + lst2[i] + lst3[i], range(len(lst1))))
print(lst) #结果为:[6, 9, 12, 15, 18]

# //todo 方法4:
lst.clear()
lst = list(map(lambda x, y, z: x + y + z, lst1, lst2, lst3))
print(lst) #结果为:[6, 9, 12, 15, 18]


# //! filter（）函数， 过滤器函数
#  示例: 现有列表range(-5, 5)， 先要求只得到正数的列表
lst = range(-5, 5)
result = [i for i in lst if i > 0]
print(result)  #结果为:[1, 2, 3, 4]

result.clear()
result = list(filter(lambda i: i >0, lst))
print(result) #结果为:[1, 2, 3, 4]

