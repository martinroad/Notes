# 列表：[]
# 字典：{}
# 集合:{}

# 浅拷贝，只拷贝第一层的
a = ['name', 123, ['python', 'php']]
b = a.copy()

a[2][0] = 'test'  # 这时候修改第二层的元素，拷贝之后的也跟着变了，也就是表示只拷贝了第一层的称为深拷贝
print(a)
print(b)

# 深拷贝，包括最里层的也拷贝了
import copy
a = ['name', 123, ['python', 'php']]
b = copy.deepcopy(a)
print(a)
print(b)

a[2][0] = 'test'
print(a)
print(b)


