import os

# 查看当前的工作目录
print(os.getcwd()) 
url = os.getcwd() + '\\文件的读写\\txt文件读写\\'+ 'test.txt'

# //! 读取文件内容
file = open(url) # 等用于 open('test.txt', 'r') 只读方式
content = file.read()
print('content:', content)
file.close()

# //! 向 test.txt 文件中写入内容
f = open(url,'a')  # ‘a’表示以写的方式打开文件，如果文件已经存在，则指针在文件的最后，实现向文件末尾追加新内容，否则，则新建文件
slen = f.write('sssssssss~~~~') # 返回所写入内容的长度
print('length：', slen)
f.close()

# //! 常见写法（使用with open 后，不需要手动close）
with open(url, 'a') as f:
    f.write('\ntest~test~')

f1 = open(url)
# f1.seek(0)  # 将文件指针移动到文件的起始位置
for line in f1:
    print(line, end='')

