
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return 'eat...'

# //! Dog 类继承 Animal 类，相当于将 Animal 类的所有代码搬到了 Dog 类
class Dog(Animal):
    pass

dog = Dog('dog')
print(dog.name)  #结果为：dog


# //! 这时候尽管Cat类继承了父类Animal类，但是有字类有与父类同名方法__init__()，子类就覆盖了父类同名的方法
class Cat(Animal):
    def __init__(self, age):
        self.age = age

cat = Cat('cat')
print(cat.age)

# //! 在字类里重写父类的方法
class Cat(Animal):
    def __init__(self, age, name):
        self.age = age
        super().__init__(name)  # 这是用  super() 代表父类 Animal 

cat = Cat(2, 'cat')
print(cat.age)
print(cat.name)



'''
单继承示例
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 获取姓名
    def get_name(self):
        return self.name

    # 获取年龄
    def get_age(self):
        return self.age

class Student(Person):
    def __init__(self,  name, age,  school):
        self.school = school
        super().__init__(name, age)

    # 设置年纪
    def grade(self, n):
        self.grade = n   
        print("{0}'s age is {1}, school is {2}".format(self.name, self.age, self.school)) 

    # 获取学校
    def get_school(self):
        return self.school

    # 获取年纪
    def get_grade(self):
        return self.grade    

student = Student('XiaoMing', 21, 'ShenZhen Normal University')
student.grade(1)

print(student.get_name())
print(student.get_age())
print(student.get_school())
print(student.get_grade())


'''
多继承示例
'''
class K1:
    def foo(self):
        print('K1 - foo')

class K2:
    def foo(self):
        print('K2 - foo')
    def bar(self):
        print('K2 - bar')    

class J1(K1, K2):
    print('- J1(K1, K2) -')

class J2(K1, K2):
    print('- J2(K1, K2) -')
    def bar(self):
        print('J2 - bar')

class T1(J1, J2):
    print('- T1(J1, J2) -')

# //! 查看T1类的继承顺序
print('T1.__mro__', T1.__mro__)
print('J1.__mro__', J1.__mro__)   
print('J2.__mro__', J2.__mro__)   

t = T1()
t.foo()
t.bar()

