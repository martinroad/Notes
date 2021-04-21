import os
import csv

# 查看当前的工作目录
print(os.getcwd()) 

# 文件路径
url = os.getcwd() + '\\文件的读写\\csv文件读写\\'+ 'test.csv'

# 要写入的内容
data = [['name', 'number'], ['python', 111], ['java', 222], ['php', 333]]

# //! 写入文件
with open(url, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# //! 读取文件
file = open(url)
reader = csv.reader(file)
for row in reader:
    print(row)     