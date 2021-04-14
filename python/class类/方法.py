# 方法和函数：
# 1、名称的命名、代码块的编写方式都一样
# 2、（实例）方法不能单独调用，只能通过实例/类来调用
# 3、方法的第一个参数必须是self

# //! 实例方法的调用，第一个参数self 就表示的是实例了  
class Foo:
    def method(self, x):
        return x * 2021
  
# //todo:方法一 
f1 = Foo()
result1 = f1.method(2)
print(result1)

# //todo:方法二
f2 = Foo()
result2 = Foo.method(f2, 2)
print(result2)


# //! 类方法的调用，在方法前面使用装饰器 @classmethod，类方法第一个参数：cls，表示类本省
class Bar:
    @classmethod
    def method(cls, x):
        return x * 1024

b = Bar()
result = b.method(2)
print(result)


# //! 静态方法调用，在方法前面使用装饰器 @staticmethod，静态方法不与实例绑定，所以不需要参数self和cls
class Car:
    @staticmethod
    def add():
        return 1024

# //todo:方法一
reuslt = Car.add()
print(reuslt)

# //todo:方法二
c = Car()
result = c.add()
print(result)


'''
创建类，能够通过 “年-月-日” 字符串创建实例，并检验年、月、日是否合法
'''
class Date(object):
    # 实例方法
    def __init__(self, year = 1970, month = 1, day = 1):
        self.year = year
        self.month = month
        self.day = day

    # 类方法
    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        date1 = cls(year, month, day)  # 调用实例方法，这里写上cls(year, month, day)，其实就是Date(year, month, day)，是为了防止如果以后将类名Date改成其他，这里也得跟着改动
        return date1

    # 静态方法
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return year<=2038 and day>0 and day<=31 and month>0 and month <=12


# 调用实例方法
d1 = Date(2021, 1, 1)
print(d1.year, d1.month, d1.day)

# 调用类方法
d2 = Date.from_string('2021-1-1')
print(d2.year, d2.month, d2.day)

# 调用静态方法
is_valid = Date.is_date_valid('2021-1-1')
print(is_valid)




        
