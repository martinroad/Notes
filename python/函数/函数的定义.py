# coding=utf-8

# //! 函数的定义，设置参数的默认值
# //! 如果函数没有用return，默认是返回None
def add(x, y = 0):
   return x + y

# //! 按照参数位置体统参数
a = add(1, 2)
print(a)

# //! 指明参数名称调用函数
a = add(x = 1, y = 2)
print(a)



# //! 返回值：
# //todo1、返回一个值
# //todo:2、返回多个值
def my_fun():
    return 1,2,3

r = my_fun()
print(r)    #结果为(1, 2, 3) 

a1, a2, a3 = my_fun() 
print(a1)    #结果为1
print(a2)    #结果为2
print(a3)    #结果为3


# //! 参数的收集：
# //todo：一个 "*" 的作用
def test1(x, *args):
    print('x = ', x)
    print('args = ', args)

test1(1,2,3,4,5)  #结果为：x =  1 , args =  (2, 3, 4, 5)
test1(1)          #结果为：x =  1 ， args =  ()
# test1(x = 1, y = 2, z = 3, k = 4)

# //todo：两个 "**" 的作用
def test2(*a, **b):
    print('a = ', a)  #结果为：a =  (1, 2, 3)
    print('b = ', b)   #结果为：b =  {'x': 1, 'y': 2, 'z': 3, 'k': 6}
test2(1,2,3,x=1,y=2,z=3,k=6)    

# //! 示例：
'''
假设有数据: d = {'a':39, 'b':40, 'c':99, 'd':100}（字典的键值对还可以增加），编写函数，实现对这个字典中键值对的查询。例如向函数提供 a = 1, b = 40 等参数，查询这些是否为此数据的值
'''
def kvfind(dct, ** kvargs):
    r = {k:v for k,v in kvargs.items() if dct.get(k) == v}
    return r

d = {'a':39, 'b':40, 'c':99, 'd':100}
fr = kvfind(d, a = 1 , b = 40)
print(fr)    #结果为{'b': 40}
