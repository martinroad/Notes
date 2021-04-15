

# //!通过私有华可以对属性或者方法进行封装，在属性或者方法名前加上两个下划线：__
class Foo:
    def __init__(self, name):
        self.name = name
        self.__group = 'test~test~'   # __group 这个属性是私有属性
    
    def get_group(self):
        return self.__group
        
    def __get_name(self):    # __get_name() 这个方法是私有方法
        return self.name


f = Foo('test~')
print(f.name)

# //todo:下面代码会报错
# print(f.__group)  

group = f.get_group()
print(group)

# //todo:下面代码会报错
# name = f.__get_name()  #结果为:AttributeError: 'Foo' object has no attribute '__get_name'
# print(name)
