# import time, pymysql
#
# # ----------------------------------------------方式1:flask 装饰器工厂模式------------------------------------------------>
# # 路由列表  路径  函数引用  flask框架添加路由
# route_list = []
#
#
# def route(url):
# 	"""装饰器工厂:接收url参数,产生装饰器"""
#
# 	def wrapper(func):
# 		# 将获取到的路径信息 函数引用添加到路由列表
# 		route_list.append((url, func))
#
# 		def inner():
# 			pass
#
# 		return inner
#
# 	return wrapper
#
#
# @route('/gettime.html')
# def gettime():
# 	return '200 OK', [('Server', 'PWS9.0')], time.ctime()
#
#
# @route('/index.html')
# def index():
# 	"""当用户请求/index.html"""
# 	# 1.读取模板文件
# 	with open('template/index.html', 'rb') as file:
# 		html_data = file.read().decode()
# 	# 2.连接数据库,取出数据
# 	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', db='py_test', charset='utf8')
# 	cur = conn.cursor()
# 	sql = "select * from info;"
# 	cur.execute(sql)
# 	data = ""
# 	# data = str(cur.fetchall())
# 	for line in cur.fetchall():
# 		data += """
# 		<tr>
#
# 		<td>%s</td>
# 		<td>%s</td>
# 		<td>%s</td>
# 		<td>%s</td>
# 		<td>%s</td>
# 		<td>%s</td>
# 		<td>%s</td>
# 		<td>%s</td>
# 		<td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
#
# 		</tr>
#
# 		""" % line
#
# 	# 3.模拟模板替换 {%content%} --> 用户需要的数据
# 	html_data = html_data.replace('{%content%}', data)
# 	return '200 OK', [('Server', 'PWS9.0')], html_data
#
#
# @route('/center.html')
# def center():
# 	"""当用户请求/index.html"""
# 	# 1.读取模板文件
# 	with open('template/center.html', 'rb') as file:
# 		html_data = file.read().decode()
# 		# 2.连接数据库,取出数据
# 		conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', db='py_test',
# 							   charset='utf8')
# 		cur = conn.cursor()
# 		sql = "select info.code," \
# 			  "info.short," \
# 			  "info.chg," \
# 			  "info.turnover," \
# 			  "info.price," \
# 			  "info.highs," \
# 			  "focus.note_info " \
# 			  "from info join focus " \
# 			  "on info.id=focus.info_id;"
# 		cur.execute(sql)
# 		data = ""
# 		# data = str(cur.fetchall())
# 		for line in cur.fetchall():
# 			data += """
# 			<tr>
#
# 			<td>%s</td>
# 			<td>%s</td>
# 			<td>%s</td>
# 			<td>%s</td>
# 			<td>%s</td>
# 			<td>%s</td>
# 			<td>%s</td>
# 			<td><a type="button" class="btn btn-default btn-xs" href="/update/000007.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
#             <td> <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="000007"></td>
#
# 			</tr>
#
# 			""" % line
#
# 	# 3.模拟模板替换 {%content%} --> 用户需要的数据
# 	html_data = html_data.replace('{%content%}', data)
# 	return '200 OK', [('Server', 'PWS9.0')], html_data
#
#
#
#
# def app(env):
# 	"""框架提供的函数 web服务器调用这个函数就可以运行"""
# 	# 当web服务器接收到动态资源请求的时候,web服务器需要调用当前这个
# 	# .html结尾的,就是动态资源
# 	print('收到来自web服务器的请求数据%s' % str(env))  # 就是用户在浏览器里面输入的地址<路径信息>,比如:127.0.0.1:8080/index.html
# 	path_info = env['PATH_INFO']
#
# 	# if env['PATH_INFO'] == '/gettime.html':
# 	# 	return gettime()
# 	# elif path_info == '/index.html':
# 	# 	return index()
#
# 	# 遍历路由列表  如果路径匹配,就执行相应的函数
# 	for url, func in route_list:
# 		if url == path_info:
# 			return func()  # 找到路径,就执行路径对应的函数功能
# 	else:  # 如果遍历完没找到,就最后一次性返回404信息
# 		# 返回值 状态 响应头 响应体
# 		return '404 Not Found', [('Server', 'PWS9.0')], 'response body:not found'
#

"""
1.web服务器怎么样将请求数据给框架:解析成一个字典传参数
2.框架怎么样将响应数据给 web 服务器的
3.app是用来干嘛的:框架提供给服务器使用的,处理动态资源,结果通过函数返回值返回
用户请求信息通过参数传进去

模板:一套空文件,装数据的
所有的框架都支持模板
好处:一个就可以装好多数据
"""
# ----------------------------------------路由:------------------------------------->
"""
路由:if...else...写多了就废了
提前把所有的路径以及路径对应的函数以元组的形式 全部 都存到一个列表中
[(),(),()]这种形式
可以保证顺序,字典是无序的
正则表达式等下要匹配
路由列表中存的是路径和函数


视图函数:index,center


股票信息的格式:
<tr>
	
</tr>

一对tr标签控制的是一行数据的显示
一对td标签控制的是一个字段数据的显示

select info.code,
info.short,
info.chg,
info.turnover,
info.price,
info.highs,
focus.note_info 
from info join focus on info.id=focus.info_id;

"""
# 模板变量-->替换为 用户所需要的数据   {%content%} ---> 用户需要的数据


# ------------------------------------------------方式2:django 列表模式------------------------------------------------>
import time, pymysql


def gettime():
	return '200 OK', [('Server', 'PWS9.0')], time.ctime()


def index():
	"""当用户请求/index.html"""
	# 1.读取模板文件
	with open('template/index.html', 'rb') as file:
		html_data = file.read().decode()
	# 2.连接数据库,取出数据
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', db='py_test', charset='utf8')
	cur = conn.cursor()
	sql = "select * from info;"
	cur.execute(sql)
	data = ""
	# data = str(cur.fetchall())
	for line in cur.fetchall():
		data += """
		<tr>

		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
		<td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>

		</tr>

		""" % line

	# 3.模拟模板替换 {%content%} --> 用户需要的数据
	html_data = html_data.replace('{%content%}', data)
	return '200 OK', [('Server', 'PWS9.0')], html_data


def center():
	"""当用户请求/index.html"""
	# 1.读取模板文件
	with open('template/center.html', 'rb') as file:
		html_data = file.read().decode()
		# 2.连接数据库,取出数据
		conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', db='py_test',
							   charset='utf8')
		cur = conn.cursor()
		sql = "select info.code," \
			  "info.short," \
			  "info.chg," \
			  "info.turnover," \
			  "info.price," \
			  "info.highs," \
			  "focus.note_info " \
			  "from info join focus " \
			  "on info.id=focus.info_id;"
		cur.execute(sql)
		data = ""
		# data = str(cur.fetchall())
		for line in cur.fetchall():
			data += """
			<tr>

			<td>%s</td>
			<td>%s</td>
			<td>%s</td>
			<td>%s</td>
			<td>%s</td>
			<td>%s</td>
			<td>%s</td>
			<td><a type="button" class="btn btn-default btn-xs" href="/update/000007.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
            <td> <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="000007"></td>

			</tr>

			""" % line

	# 3.模拟模板替换 {%content%} --> 用户需要的数据
	html_data = html_data.replace('{%content%}', data)
	return '200 OK', [('Server', 'PWS9.0')], html_data


# -----------方式2:django---------------------->
# 路由列表  路径  函数引用  django框架添加路由
route_list = [
	('/gettime.html', gettime),
	('/index.html', index),
	('/center.html', center),
]


def app(env):
	"""框架提供的函数 web服务器调用这个函数就可以运行"""
	# 当web服务器接收到动态资源请求的时候,web服务器需要调用当前这个
	# .html结尾的,就是动态资源
	print('收到来自web服务器的请求数据%s' % str(env))  # 就是用户在浏览器里面输入的地址<路径信息>,比如:127.0.0.1:8080/index.html
	path_info = env['PATH_INFO']

	# if env['PATH_INFO'] == '/gettime.html':
	# 	return gettime()
	# elif path_info == '/index.html':
	# 	return index()

	# 遍历路由列表  如果路径匹配,就执行相应的函数
	for url, func in route_list:
		if url == path_info:
			return func()  # 找到路径,就执行路径对应的函数功能
	else:  # 如果遍历完没找到,就最后一次性返回404信息
		# 返回值 状态 响应头 响应体
		return '404 Not Found', [('Server', 'PWS9.0')], 'response body:not found'


# ------------------------------个人中心js模板:----------------------->
"""
<tr>
            <td>000007</td>
            <td>全新好</td>
            <td>10.01%</td>
            <td>4.40%</td>
            <td>16.05</td>
            <td>14.60</td>
            <td></td>
            <td><a type="button" class="btn btn-default btn-xs" href="/update/000007.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
            <td> <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="000007"></td>
            </tr>

"""
