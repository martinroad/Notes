# coding=utf-8


class SuperMan:
    '''
    A class of SuperMan
    '''

    # 初始化函数
    def __init__(self, name):   
        self.name = name
        self.gender = 1
        self.single = False
        self.illness = False

    # 普通函数
    def nine_negative_kungfu(self):
        return "Ya! You have to die."


# 类的调用，输出类的属性
guojing = SuperMan('guojing')
print('guojing.name:', guojing.name)
print('guojing.gender:', guojing.gender)
print('guojing.single:', guojing.single)
print('guojing.illness:', guojing.illness)

# 类的函数的调用
print('guojing.nine_negative_kungfu:', guojing.nine_negative_kungfu())



'''
测试类的定义，类属性和实例属性
'''
class Foo:
    lang = 'python'

# 类的属性
print(Foo.lang)

# 实例的属性
f = Foo()
print(f.lang)


'''
示例：创建类，能够实现任意两个日期之间的天数和周数
准备：pip3 install python-dateutil
'''
import datetime
from dateutil import rrule

class BetweenDate:
    def __init__(self, start_date, end_date):
        self.start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    def days(self):
        d = self.end - self.start
        return d.days

    def weeks(self):
        week = rrule.rrule(rrule.WEEKLY, dtstart = self.start, until = self.end )
        print(week)
        return week.count


fir_twe = BetweenDate('2021-4-01', '2021-4-01')
d = fir_twe.days()
week = fir_twe.weeks()

print('days:', d)
print('weeks:', week)






