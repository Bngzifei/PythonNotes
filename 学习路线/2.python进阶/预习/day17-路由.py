"""
为啥需要路由?
如果我们的框架处理的页面请求路径再多一些,比如5个大家可能感觉条件分支完全可以胜任,如果是40个甚至更多呢?如果这是还是用普通的条件分支简直无法忍受

理解:意思就是将用户的各种可能性的选择进行了if条件的判断选择谈繁琐了,应该专门有一个模块来专门处理这种可能性的选择判断.所以出现了路由列表的 概念
请求路径			执行代码
/login.html		login()
/logout.html	logout()
/gettime.html	gettime()
"""
"""
如何实现?
代码中实现的思路就是将所有的路径和路径对应的执行代码提前放置在路由列表中,待用户请求过来了直接执行请求路径对应的函数即可.
"""
import time
import re

# ---------------------更新------------------->
# 用来存放url路由映射
# url_route = [
# 	('/index.py',index_func),
# 	('/center.py',center_func),
# 	()
# ]
g_url_route = list()

def route(url):
	def func1(func):
		# 添加键值对,key是需要访问的url,value是当这个url需要访问的时候,需要调用的函数引用
		g_url_route.append((url,func))
		def func2(file_name):
			return func(file_name)
		return func2
	return func1

@route('/index.html')
def index():
	pass





