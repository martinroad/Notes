# 集合的定义，用{}表示，集合中的元素是没有顺序的，无序性
a = set([1,2,3,4,5])
print(a)
a = {1,2,3,4,5,'python', 'a', 3.14}
print(a)


# 向集合中增加元素
a.add(100)
print(a)

# 删除集合中的指定元素remove方法
a.remove('python')
print(a)

# discard 也是从集合中删除指定元素，如果python这个元素不在集合中，用discard删除不会报错，但是用remove删除会报错
a.discard('python')
# a.remove('python')

# pop 是从左往右移除集合的第一个元素
a.pop();
print(a)

# 下面这样会报错，因为列表[100,200]是不可哈希的，因为列表是可变对象，不能用可变对象作为集合的元素
# 集合的元素必须是不可变对象
# b = {1,2,3,4,5,'python', 'a', 3.14, [100, 200]}
# print(b)


# 创建不可变集合
f_set = frozenset('abcdef')
print('f_set=>', f_set)


# 集合与集合的关系：超集/子集
c = {1, 2, 3, 4, 5 }
d = {1, 2, 3}
print(c.issuperset(d))
print(d.issubset(c))

# 集合之间的并集
print('c | d=>', c | d)
print('c.union(d)=>', c.union(d))
# 集合之间的交集
print('c & d=>', c & d)
print('c.intersection(d)=>', c.intersection(d))
# 集合之间的差集
print('c - d=>', c - d)
print('c.difference(d)=>', c.difference(d))