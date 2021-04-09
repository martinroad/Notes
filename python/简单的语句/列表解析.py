
# 要求将0~9这10个数字的平方写入列表

lst = []
for i in range(10):
    lst.append(i**2)
print(lst)

lst.clear()
lst = [i**2 for i in range(10)]
print(lst)

# //!示例1： 得到100以内能被3整除的正整数
a = [i for i in range(100) if i %3 ==0]
print(a)

# 已知字符串 b = 'Life is short, you need to know how to cherish'，统计这个字符串中每个单词的字母数量
b = 'Life is short, you need to know how to cherish'

# //todo 1、统计单词的字符数：[('Life', 4), ('is', 2), ('short,', 6), ('you', 3), ('need', 4), ('to', 2), ('know', 4), ('how', 3), ('to', 2), ('cherish', 7)]
result = []
b = b.split(" ")  #结果为：['Life', 'is', 'short,', 'you', 'need', 'to', 'know', 'how', 'to', 'cherish']
print(b)
for c in b:
    result.append((c, len(c)))
print(result)    

# //todo 统计字符串中每个英文字母的数量
b = 'Life is short, you need to know how to cherish'

d ={}
for c in b:
    if c.isalpha(): # isalpha是一种函数：判断字符ch是否为英文字母，若为英文字母，返回非0（小写字母为2，大写字母为1）。若不是字母，返回0
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
print(d)            







