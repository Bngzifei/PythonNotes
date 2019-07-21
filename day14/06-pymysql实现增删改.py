"""
1.>创建连接connection
2.>获取cursor游标
3.>增删改查等操作
4.>commit()提交
5.>关闭cursor游标
6.>关闭连接connection
"""
import pymysql

# 1.创建和数据库服务器的连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', database='python_test_1',
					   charset='utf8')
# 2.获取游标
cur = conn.cursor()
# 3.执行sql
sql = 'update students set age=59 where id=1;'
row_count = cur.execute(sql)  # 参数1是sql语句,返回值是sql语句影响的行数
print('影响了%d行' % row_count)
# 提交修改   ---修改之后必须提交才会生效,否则不会发生改变
conn.commit()
sql = 'select age from students where id=1;'
cur.execute(sql)
# 取出((字段,),(),())
# print(cur.fetchall())  # 全部取出来
# print(cur.fetchall())  # 全部取出来
print(cur.fetchone())  # 取出一条数据  (1, '小明', 18, Decimal('180.00'), '女', 1, b'\x00')
print(cur.fetchone())  # 取出一条数据  (2, '小月月', 18, Decimal('180.00'), '女', 2, b'\x01')
# 4.关闭游标
cur.close()
# 5.关闭连接
conn.close()
