
import pymysql
from pymysql import Error

host_name = 'localhost'
user_name = 'root'
passwd = '123456'
database_name = 'python_db'

# 简历一个数据库连接
def create_connection():
        try:
                connection = pymysql.connect(host=host_name,
                                     user=user_name,
                                     password=passwd,
                                     database=database_name)
                print('connect mysql successful ...')
                return connection
        except Error as e:
                print('Error：', e)

# 执行数据库写操作，返回操作影响的行数
def execute_write_query(db, sql):
        try:
                cursor = db.cursor()  #使用 cursor() 方法创建一个游标对象 cursor
                result = cursor.execute(sql)
                db.commit()
                return result
        except Error as e:
                print('execute_write_query error:', e)

# 执行数据库读操作
def execute_read_query(db, sql):
        result = None
        try:
                cursor = db.cursor() #使用 cursor() 方法创建一个游标对象 cursor
                cursor.execute(sql)
                result = cursor.fetchall()
        except Error as e:
                print('execute_read_query error:', e)
        finally:
            return result