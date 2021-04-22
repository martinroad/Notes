'''
    使用Python内置的 SQLite3 内置数据库
    SQLite3 可使用 sqlite3 模块与 Python 进行集成，您不需要单独安装该模块，因为 Python 2.5.x 以上版本默认自带了该模块
'''

import sqlite3

path = './sqlitedb/db.sqlite'

# 1、该 API 打开一个到 SQLite 数据库文件 database 的链接
connection = sqlite3.connect(path)
# 2、创建一个 cursor
cour = connection.cursor() 

# 3、sql语句，创建一个名为 users 的表
create_sql = """
    create table if not exists users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name text not null,
        age INTEGER,
        gender text
    );
"""

# 4、执行 创建表的sql语句
cour.execute(create_sql)

# 4、清空数据表 users 中的所有数据
delete_sql ="""
    delete from users;
"""
cour.execute(delete_sql)
connection.commit()

# 5、向 users 表中插入数据
inster_sql ="""
    insert into users(name, age, gender) values
    ('张三', 20, 'male'),
    ('李四', 20, 'female'),
    ('王五', 20, 'male');
"""
cour.execute(inster_sql)

# 6、对数据库表进行修改后，一定要执行connection.commit（）操作
connection.commit()

# 7、查询users表中的数据
select_sql ="""
    select * from users where id = 1
"""
cour.execute(select_sql)
result = cour.fetchall()
connection.close()
print(result)




