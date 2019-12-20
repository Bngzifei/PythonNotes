print('python代码自动化处理sql语句')
"""
pymysql就是一种客户端
1.>创建连接connection
2.>获取cursor游标
3.>增删改查等操作 
4.>关闭cursor游标
5.>关闭连接connection

类似过河拆桥.
游标依赖于连接
游标的底层就是连接

"""
import pymysql

# 1.创建和数据库服务器的连接  主机/端口/用户名/密码/数据库/通信的字符集  建议和数据库创建的字符集保持一致
# charset='utf8' 表示通信的编码格式
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='password',database='python_test_1',charset='utf8')

# 2.获取游标
cur = conn.cursor()
# 3.执行sql
sql = 'select * from students;'
cur.execute(sql)
# 取出((字段,),(),())
print(cur.fetchall())  # 全部取出来
print(cur.fetchall())  # 全部取出来
print(cur.fetchone())  # 取出一条数据
print(cur.fetchone())  # 取出一条数据
# 4.关闭游标
cur.close()
# 5.关闭连接
conn.close()