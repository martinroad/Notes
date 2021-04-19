

# //! 测试import module后，不打印被引入module的调试日志信息
import book

b = book.Book('python')

# 查看模块的属性列表
print(dir(b))

author = b.get_author()
print('author->:', author)


# //! 查看import module 的搜索路径
import sys
print(sys.path) #结果为['d:\\ANotes\\Notes\\python\\python����ģ��\\ģ��', 'C:\\ProgramData\\Anaconda3\\python37.zip', 'C:\\ProgramData\\Anaconda3\\DLLs', 'C:\\ProgramData\\Anaconda3\\lib', 'C:\\ProgramData\\Anaconda3', 'C:\\Users\\Administrator\\AppData\\Roaming\\Python\\Python37\\site-packages', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32\\lib', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\Pythonwin']

# //! 如果被引入的module 不和本文件在同一个路径下，则需要 sys.path.append('路径')
sys.path.append('D:\\ANotes\\Notes\\python')
print(sys.path)





