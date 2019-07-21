print('---------------------------------')
# import pymysql
#
# conn = pymysql.connect(host='localhost', port=3306, user='root', password='password',
# 					   database='python_test_1', charset='utf8')
#
# cursor = conn.cursor()
#
# # sql = """delete from students WHERE NAME ='西部坏蛋孙悟空';"""
# # sql = """select * from students where name='西部坏蛋孙悟空';"""
# # sql = """insert into students (name) VALUE ('西部坏蛋孙悟空')"""
# sql = """update students set height=175 WHERE id=10"""
# row_count = cursor.execute(sql)
# print('SQL语句执行影响的行数%d' % row_count)
# print(cursor.fetchall())
#
# conn.commit()
# for line in cursor.fetchall():
# 	print(line)
# conn.rollback()
#
#
#
# cursor.close()
# conn.close()
# -----------------------------------参数化列表防止SQL注入----------------->
"""
SQL注入产生原因:后台将用户提交的带有恶意的数据和SQL进行字符串方式的拼接,从而影响
了SQL语句的语义,最终产生数据泄露的现象.

如何防止?
sql语句的参数化,将sql语句的所有数据参数存在一个列表中传递给execute函数的第二个参数
注意:此处不同于python的字符串格式化,必须全部使用%s占位
所有参数所需占位符外不需要加引号.

"""

from pymysql import connect


def main():
	find_name = input('输入人名:')

	# 创建connnection连接
	conn = connect(host='localhost', port=3306, user='root', password='password',
				   database='py_20')
	# 获得cursor对象
	cs1 = conn.cursor()

	# 非安全方式
	sql = 'select * from info where short = "%s"' % find_name
	print("""sql====>%s<===""" % sql)
	count = cs1.execute(sql)

	# 安全的方式
	# 1.构造参数列表
	# params = [find_name]
	# #执行select 语句,并返回受影响的行数:查询所有数据
	# count = cs1.execute('select * from info where short=%s',params)
	# 注意:
	# 如果要是有多个参数,需要进行参数化
	# 那么params = [数值1,数值2...] ,此时sql语句中有多个%s即可
	# 打印受影响的行数
	print(count)
	# 获取查询结果
	result = cs1.fetchall()
	print(result)

	# 关闭cursor对象
	cs1.close()
	# 关闭connection对象
	conn.close()


if __name__ == '__main__':
	main()
