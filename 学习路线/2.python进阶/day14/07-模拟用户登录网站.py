import pymysql

# 建立连接
conn = pymysql.connect(host='localhost', port=3306,user='root', password='password', db='jd', charset='utf8')
cur = conn.cursor()

name = input('请输入用户名:')
password = input('输入密码:')

# sql手动拼接sql语句,往往容易造成sql注入
# 用户输入的数据往往带有恶意
# sql = "select * from hero where name = '%s' and kongfuid = %s" % (name, password)
# print(sql)
# 这样就是sql注入了.把数据库的核心暴露了
# select * from hero where name = '妲己' or 1=1 #' and kongfuid = 4545
# 成功登录 (1, '妲己', 2)

# 解决sql注入的手段--->参数化列表 :1.>sql中的%s就不需要''引号了,只能使用%s  2.>参数全部放到列表中,参数也不要在这里了,放到列表中,在cur.execute()的时候传进去
sql = "select * from hero where name = %s and kongfuid = %s"

# 把sql语句需要的所有参数放到一个列表中,把这个列表当做第二个参数传给execute


# 查看参数化列表的结果
print(cur.mogrify(sql, [name, password]))
# name = '妲己\' 里面的\将'进行了转义,这样就可以把'这个匹配功能给屏蔽掉了.
# select * from hero where name = '妲己\' or 1 # ' and kongfuid = '5656'
# 登录失败

# 执行sql
row_count = cur.execute(sql, [name, password])
# row_count = cur.execute(sql)

if row_count > 0:
	print('成功登录', cur.fetchone())
else:
	print('登录失败')

cur.close()
conn.close()
"""
sql注入的问题 ----> 产生了数据泄露
解决办法:---> 参数化列表,取消'%s'的格式,一律使用%s进行占位,把参数放进列表

问题:输入 妲己' or 1=1 # 因为or 1=1 永远成立 的关系,造成短路了


请输入用户名:妲己' or 1 # 
输入密码:5656
select * from hero where name = '妲己' or 1 # ' and kongfuid = 5656
成功登录 (1, '妲己', 2)

"""
