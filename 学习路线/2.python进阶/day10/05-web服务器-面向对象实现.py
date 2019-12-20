"""
PWS5.0目的:使用协程实现多任务,提高体验

1.>接收请求报文
2.>解析请求报文-得到用户需求
3.>根据用户的需求找到对应的资源
4.>资源打包到HTTP响应报文

最开始肯定是最简单的,一步一步的加多,慢慢地才会出来
PWS2.0:Python Web Server 2.0

主从
master slave

主:接受用户数据
从:干活

leader:
follower:



"""
import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()  # 自动切换  time.sleep recv accept 这些类型的函数在执行的时候会出现大量的耗时等待,所以让这部分闲置时间加以利用.





class HTTPServer:
	"""web服务"""

	def __init__(self):
		"""初始化操作"""
		# 1. 创建tcp服务器的socket  设置选项 绑定 监听
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server_socket.bind(('', 8999))  # 这里绑定的是服务器的固定端口,目的是让客户端能连接到了我的机器上面之后,可以找到我的这个程序
		server_socket.listen(128)

		# 将socket对象保存在 当前对象的属性中
		self.server_socket = server_socket

	def start(self):
		"""启动服务"""
		while True:
			client_socket, client_addr = self.server_socket.accept()
			print('接受到%s的连接请求' % str(client_addr))
			# 为每个用户创建一个协程,并且启动 运行
			gevent.spawn(self.client_handler, client_socket)

	def client_handler(self,client_socket):
		"""处理每个客户端的请求"""
		# 3.接收用户请求报文
		request_data = client_socket.recv(4096)
		# 解码 bytes  --> str
		request_data_str = request_data.decode()
		print(request_data)
		# ps:当用户的请求路径为/时候,表示其请求的是首页homepage
		# 解析用户请求 获取到用户的资源请求路径
		# 正则匹配 只要是有/ 提取请求路径
		# GET /index.html
		result = re.search(r'^\w+ (/\S*)', request_data_str)
		# 判断是否提取成功  成功就取出这个值,不成功结束程序
		if not result:  # 路径为空
			print('请求报文格式错误')
			client_socket.close()
			return  # 结束 这种情况
		# 尽量扁平结构 不要使用else缩进去,那样的是嵌套结构,这是小技巧
		# 获取请求路径  资源路径<static> + /index.html
		# 如果执行到这里,一定是匹配成功了,因为失败的已经跳过了
		path_info = result.group(1)
		# 4.返回用户指定的文件数据作为响应体   打包到响应报文中  static + /index.html
		# static 是文件夹,open打不开 潜规则 :所有的web服务器 不写路径默认是主页

		# 如果path_info 是/ ,返回 index首页
		if path_info == '/':
			path_info = '/index.html'

		try:
			with open('static' + path_info, 'rb') as file:
				html_data = file.read()  # html_data 是二进制bytes字节类型的数据
		except Exception as e:
			with open('404.html', 'rb') as file:
				html_data = file.read()
			response_data = ('HTTP/1.1 404 Not Found\r\nServer: PWS3.0Plus\r\n\r\n').encode() + html_data
		else:
			# .encode()先把前面的str类型转成bytes字节类型,然后拼接
			response_data = ('HTTP/1.1 200 OK\r\nServer: PWS3.0Plus\r\n\r\n').encode() + html_data

		finally:
			# 统一最后发送
			client_socket.send(response_data)
			# 5.一次请求/响应 就关闭连接  --> 短连接
			client_socket.close()


if __name__ == '__main__':
	# 创建web服务
	http_server = HTTPServer()
	# 启动web服务
	http_server.start()


"""
总结:
	# 封装 方法和属性封装在一个类中
	# 继承 功能扩展 快速获取技能
	# 多条 一种形式的多种状态

	# 面向过程  吃狗屎  吃(狗,屎)
	# 面向对象  狗吃屎   狗.吃(翔)
"""



