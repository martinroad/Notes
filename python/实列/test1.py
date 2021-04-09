# 已知列表[1,2,3,4,5,6,7,8,9],要求得到：
# 1、得到偶数
# 2、得到奇数
# 3、得到[9,7,5,4,3,1]
# 4、得到[1,2,3,4]
# 4、得到[4,3,2,1]


a = [1,2,3,4,5,6,7,8,9]
a_1 = [] 
a_2 = []
a_3 = [] 
a_4 = []
a_5 = [] 

for i in a:
    if  i % 2 ==0:
        a_1.append(i)
    else:
        a_2.append(i)
print(a_1)
print(a_2)     


a_3 = a.copy() # 浅拷贝
a_3.reverse() # 反序
b = [8,6,2]
for i in b:
    a_3.remove(i)
print(a_3)

a_4 = a[:4:]
print(a_4)

a_5 = a[3::-1]
print(a_5)