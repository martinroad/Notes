
import mysql_util

# 1、创建数据表
create_sql ="""
    CREATE TABLE IF NOT EXISTS users(
	`id` INT AUTO_INCREMENT,
	`user_name` VARCHAR(100) NOT NULL,
    `age` INT,
    `sex` BOOL,
    PRIMARY KEY(`id`)
    );
"""

db = mysql_util.create_connection()
write_result = mysql_util.execute_write_query(db, create_sql)

# 2、向表中插入数据
inster_sql ="""
    insert into users(`user_name`, `age`, `sex`) values
    ('张三', 20, 0),
    ('李四', 20, 1),
    ('王五', 20, 0);
"""
insert_result = mysql_util.execute_write_query(db,inster_sql)
print('insert_result:', insert_result)


# 3、查询
select_sql ="""
    select * from users where id = 1
"""
select_result = mysql_util.execute_read_query(db,select_sql)
print('select_sql:', select_result)

# 关闭数据库连接
db.close()