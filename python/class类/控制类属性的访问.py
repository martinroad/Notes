# 控制类属性访问的三种方式:
# 1、优化内存: __slots__ 
# 2、掌握与属性相关的特殊方法:
#     __getattr__
#     __setattr__

# //! __slots__ 的作用是控制类的属性，不让随意增删，下面示例表示Bar类只有name和age两个属性，而且是只读的
class Bar:
    pass
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age 

# //! 查看Bar类字典对象
print(Bar.__dict__)

b = Bar('test', 10)
# print(b.__dict__)
print(b.name)
print(b.age)

# 下面代码会报错：'Bar' object has no attribute 'sex'
# b.sex = 1
# print(b.sex)



# //! 访问不存在的类属性，__getattr__，__setattr
class A:
    def __getattr__(self,name):
        print('__getattr__')
    def __setattr__(self, name,value):
        print('__setattr__')
        self.__dict__[name] = value

# //todo: 由于类A没有属性x，所以访问a.x 这个属性是不存在的，这是就被 __getattr__ 方法给过滤掉了
a = A()
print(a.x) 
a.x = 100
print(a.x)
