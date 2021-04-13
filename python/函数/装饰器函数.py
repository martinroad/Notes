
# //! 一层装饰器
def p_deco(func):
    def warpper(name):
        return "<p>{0}</p>".format(func(name))
    return warpper

@p_deco
def book(name):
    return "the name of my book is {0}".format(name)

result = book('~python~')
print (result)    



# //! 两层装饰器
def test1(func):
    def warpper(name):
        return "<p>{0}</p>".format(func(name))
    return warpper

def test2(func):
    def warpper(name):
        return "<div>{0}</div>".format(func(name))
    return warpper    


@test1
@test2
def test3(name):
    return "the name of my book is {0}".format(name)

test_result = test3('test')
print(test_result)


# ======================================================================================
# ======================================================================================
'''
示例：编写一个用于测试函数执行时间的装饰器函数
'''

# //todo:示例一
import time

def timing_func(func):
    def warpper(count):
        start = time.time()
        func(count)
        end = time.time()
        return end - start
    return warpper

#  测试列表的append方法执行时间
@timing_func
def test_list_append(count):
    lst= []
    for i in range(count):
        lst.append(i)

# 测试列表解析方法执行时间
@timing_func
def test_list_compare(count):
   lst = [i for i in range(count)]

count = 10000000
a = test_list_append(count) 
b = test_list_compare(count)
print('test_list_append:' , a)
print('test_list_compare:' , b)
  

# //todo:示例二
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def warpper(*args, **kvargs):
        start = time.time()
        func(*args, ** kvargs)
        end = time.time()
        print(func.__name__, (end - start))
    return warpper

@timethis
def count_down_this(count):
    while count > 0:
        count -= 1

@timethis
def test_list_append_this(count):
    lst = []
    for i in range(count):
        lst.append(i)

@timethis
def test_list_compare_this(count):
    lst = [i for i in range(count)]


count = 10000000
a1 = count_down_this(count) 
a2 = test_list_append_this(count) 
a3 = test_list_compare_this(count)
