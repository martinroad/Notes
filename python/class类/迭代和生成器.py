

# //! 如何判断某个对象是否可迭代的，就是判断其是否具有 '__iter__' 属性
# 例如判断list是否是可迭代对象
is_true = hasattr(list, '__iter__')
print(is_true) #结果为:True


#//! 迭代器对象
lst = [1, 2, 3, 4, 5]
print(hasattr(lst, '__iter__'))   #结果为:True
print(hasattr(lst, '__next__'))   #结果为:False，说明 lst 没有 __next__ 方法，不是迭代器对象

iter_lst = iter(lst)
print(hasattr(iter_lst, '__iter__'))   #结果为:True
print(hasattr(iter_lst, '__next__'))   #结果为:True，说明 iter_lst 有 __next__ 方法，是迭代器对象
print(iter_lst.__next__()) #结果为:1

# //! 创建迭代器对象 itertools.count()
import itertools
counter = itertools.count(start=7,step=2)
print('next(counter):', next(counter)) 
# for i in counter:
#     print('i:',i)


#//! 生成器函数：yield 挂起执行
def y_yield(n):
    print('start')
    while n > 0:
        print('before yield')
        yield n
        n -= 1
        print('after yield')

yy = y_yield(5)
# print(list(yy))
# print(next(yy))

for i in yy:
    print('i:', i)


# //! 生成器解析方式
lst = [x**2 for x in range(10)] # 取x得平方
print(lst)  #结果为：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

iter_lst = (x**2 for x in range(10))
print(iter_lst.__next__())  #结果为：0

for i in iter_lst:
    print('i-->:', i)
