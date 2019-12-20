# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', db='person', charset='utf8')
# cur = conn.cursor()
#
# with open(r'F:\黑马Python20期就业班\day15\person.txt', 'r', encoding='utf-8', errors='ignore') as file:
# 	while True:
# 		try:
# 			line = file.readline().strip()
# 			# print(line)
# 			# if line == '':
# 			if not line:  # 如果为空,结束循环
# 				break
# 			name = line.split(':')[0]
# 			# print(name)
# 			email = line.split(':')[1]
# 			password = line.split(':')[2]
# 			phone = line.split(':')[3]
# 			birth = line.split(':')[4]
# 			# print(birth)
# 			sql = "insert into person_info value(0,%s,%s,%s,%s,%s);"
# 			cur.execute(sql, [name, email, password, phone, birth])
# 			conn.commit()
# 		# sql = "select * from person_info;"
#
# 		except Exception as e:
# 			print('数据有误')
#
# cur.close()
# conn.close()
"""
查看倒数10个:
select * from person_info order by id desc limit 10;

+--------+-----------+--------------------+-------------+-------------+------------+
| id     | name      | email              | password    | phone       | birth      |
+--------+-----------+--------------------+-------------+-------------+------------+
| 131414 | 陈洪渝    | fireman_39@163.com | 1981716asr  | 15911227304 | 1981-07-16 |
| 131413 | 陈广法    | 510345446@qq.com   | 59472195l   | 15006591660 | 1989-09-15 |
| 131412 | 郑洪权    | 369615482@qq.com   | zheng1q8q   | 18245025627 | 1988-02-22 |
| 131411 | 陈奕良    | 369781728@qq.com   | cyl8o120o   | 13516177968 | 1986-12-06 |
| 131410 | 王美霞    | 9718210@qq.com     | sb123sb     | 18992360664 | 1984-04-08 |
| 131409 | 宋化龙    | 651920528@qq.com   | sonshualons | 18818330195 | 1988-03-06 |
| 131408 | 张永洪    | 120892313@qq.com   | 8928008m    | 15328687440 | 1994-07-25 |
| 131407 | 李健生    | 56263789@qq.com    | qewsdm      | 13395037595 | 1984-03-05 |
| 131406 | 田巧中    | tianqiao25@163.com | 526131r     | 13783451738 | 1988-03-19 |
| 131405 | 徐欣颀    | 1227261120@qq.com  | q1w2e3rp    | 15144453104 | 1989-04-01 |
+--------+-----------+--------------------+-------------+-------------+------------+
"""
"""
#create table info(
id int unsigned primary key auto_increment,
name varchar(32) not null,
email varchar(32) not null,
password varchar(32) not null DEFAULT '123456',
phone char(11) not null ,
birth date not null
);
"""

import pymysql
import re


def main():
	# 1.建立连接 获取游标
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', db='person', charset='utf8')
	cur = conn.cursor()
	# 2.打开文件 一边读取文件,一边操作数据库
	with open(r'person.txt', 'r', encoding='utf-8') as file:
		while True:
			data = file.readline().strip()
			if not data:
				break
			result = re.match(r'(.+):(.+):(.+):(\d{11}):(\d{8})', data)
			# print(result.group(1, 2, 3, 4, 5))
			if not result:  # 没有匹配到就跳过
				continue
			# 3.执行sql语句,md,这种正则的就是快啊!!!
			sql = "insert into info values(0,%s,%s,%s,%s,%s)"
			cur.execute(sql,result.group(1, 2, 3, 4, 5))

		conn.commit()
		cur.close()
		conn.close()


if __name__ == '__main__':
	main()

"""
# truncate table 表名;--->清空表数据
html可以是一个静态的资源,也可以是一个动态资源.
框架一般不处理静态资源.
"""
