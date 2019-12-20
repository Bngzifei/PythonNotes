"""
返回固定数据:
"""
# import socket
#
# tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
#
# tcp_server_socket.bind(('',9090))
#
# tcp_server_socket.listen(128)
#
# while True:
# 	# 等待客户端连接服务器
# 	server_client_socket,ip_port = tcp_server_socket.accept()
# 	# 获取客户端请求的数据报文
# 	client_request_data = server_client_socket.recv(4096)
# 	print(client_request_data)
#
# 	# 不关心请求什么数据,统一返回固定数据
# 	response_line = 'HTTP/1.1 200OK\r\n'
# 	response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
# 	response_body = '<h1>hello world!!! 你好啊,世界</h1>'
#
# 	# 拼接响应报文数据
# 	response_content = response_line + response_header + '\r\n' + response_body
# 	server_client_socket.send(response_content.encode())
# 	server_client_socket.close()

"""
返回固定页面数据
"""

# import socket
#
# if __name__ == '__main__':
#
# 	# 创建socket
# 	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	# 设置socket端口,立即释放端口
# 	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 	# 绑定端口号
# 	tcp_server_socket.bind(('', 9090))
# 	# 设置监听
# 	tcp_server_socket.listen(128)
# 	# 循环接收客户端的连接请求
# 	while True:
# 		# 等待客户端连接服务器
# 		server_client_socket, ip_port = tcp_server_socket.accept()
# 		# 获取客户端请求的数据报文
# 		client_request_data = server_client_socket.recv(4096)
# 		print(client_request_data)
#
# 		# 读取指定文件数据
# 		# 使用rb的原因是浏览器也有可能请求的是图片等等类型的文件
# 		with open('index.html','rb') as file:
# 			file_data = file.read()
#
#
# 		# 准备响应报文数据
# 		# 响应行
# 		response_line = 'HTTP/1.1 200OK\r\n'
# 		# 响应头
# 		response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
# 		# 响应体
# 		response_body = file_data
#
# 		# 匹配响应报文数据
# 		response_data = (response_line + response_header + '\r\n').encode() + response_body
# 		server_client_socket.send(response_data)
# 		server_client_socket.close()
"""
返回指定页面数据
"""
# import socket
# import re
# if __name__ == '__main__':
#
# 	# 创建socket
# 	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	# 设置socket端口,立即释放端口
# 	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 	# 绑定端口号
# 	tcp_server_socket.bind(('', 9090))
# 	# 设置监听
# 	tcp_server_socket.listen(128)
# 	# 循环接收客户端的连接请求
# 	while True:
# 		# 等待客户端连接服务器
# 		server_client_socket, ip_port = tcp_server_socket.accept()
# 		# 获取客户端请求的数据报文
# 		client_request_data = server_client_socket.recv(4096)
# 		#
# 		client_request_content = client_request_data.decode()
# 		match_obj = re.search(r'/\S*',client_request_content)
# 		# 获取匹配结果
# 		request_path = match_obj.group()
# 		print(request_path)
#
# 		if request_path == '/':
# 			# 如果用户没有指定资源路径,那么默认访问的数据是首页的数据
# 			request_path = '/index.html'
#
#
# 		# 读取指定文件数据
# 		# 使用rb的原因是浏览器也有可能请求的是图片等等类型的文件
# 		with open('static'+ request_path,'rb') as file:
# 			# 读取文件数据
# 			file_data = file.read()
#
#
# 		# 准备响应报文数据
# 		# 响应行
# 		response_line = 'HTTP/1.1 200OK\r\n'
# 		# 响应头
# 		response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
# 		# 响应体
# 		response_body = file_data
#
# 		# 匹配响应报文数据
# 		response_data = (response_line + response_header + '\r\n').encode() + response_body
# 		server_client_socket.send(response_data)
# 		server_client_socket.close()

"""返回404页面数据:"""
# import socket
# import re
#
#
# def main():
# 	# 创建socket
# 	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	# 设置socket端口,立即释放端口
# 	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 	# 绑定端口号
# 	tcp_server_socket.bind(('', 9090))
# 	# 设置监听
# 	tcp_server_socket.listen(128)
# 	# 循环接收客户端的连接请求
# 	while True:
# 		# 等待客户端连接服务器
# 		server_client_socket, ip_port = tcp_server_socket.accept()
# 		# 获取客户端请求的数据报文
# 		client_request_data = server_client_socket.recv(4096)
#
# 		client_request_content = client_request_data.decode()
# 		# 通过正则查找请求的资源路径
# 		match_obj = re.search(r'/\S*', client_request_content)
# 		# 判断路径匹配失败后的操作
#
# 		if not match_obj:
# 			print('访问路径有误')
# 			server_client_socket.close()
# 			return
#
# 		# 获取匹配结果
# 		request_path = match_obj.group()
# 		print(request_path)
#
# 		if request_path == '/':
# 			# 如果用户没有指定,据默认访问首页
# 			request_path = '/index.html'
#
# 		try:
# 			# 读取指定文件数据
# 			# 使用rb的原因是浏览器也有可能请求的是图片等等类型的文件
# 			with open('static' + request_path, 'rb') as file:
# 				# 读取文件数据
# 				file_data = file.read()
# 		except Exception as e:
#
# 			# 准备响应报文数据
# 			# 响应行
# 			response_line = 'HTTP/1.1 404 Not Found\r\n'
# 			# 响应头
# 			response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
# 			# 响应体
# 			response_body = '很抱歉,页面不存在'.encode()
#
# 			# 匹配响应报文数据
# 			response_data = (response_line + response_header + '\r\n').encode() + response_body
# 			server_client_socket.send(response_data)
# 		else:
# 			response_line = 'HTTP/1.1 200 OK\r\n'
# 			# 响应头
# 			response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
# 			# 响应体
# 			response_body = file_data
#
# 			# 匹配响应报文数据
# 			response_data = (response_line + response_header + '\r\n').encode() + response_body
# 			server_client_socket.send(response_data)
# 		finally:
# 			server_client_socket.close()
#
#
# if __name__ == '__main__':
# 	main()

"""多任务的web服务器"""
# import socket
# import re
# import gevent
# from gevent import monkey
# monkey.patch_all()
#
# def handle_client_request(server_client_socket):
# 		# 获取客户端请求的数据报文
# 		client_request_data = server_client_socket.recv(4096)
#
# 		client_request_content = client_request_data.decode()
# 		# 通过正则查找请求的资源路径
# 		match_obj = re.search(r'/\S*', client_request_content)
# 		# 判断路径匹配失败后的操作
#
# 		if not match_obj:
# 			print('访问路径有误')
# 			server_client_socket.close()
# 			return
#
# 		# 获取匹配结果
# 		request_path = match_obj.group()
# 		print(request_path)
#
# 		if request_path == '/':
# 			# 如果用户没有指定,据默认访问首页
# 			request_path = '/index.html'
#
# 		try:
# 			# 读取指定文件数据
# 			# 使用rb的原因是浏览器也有可能请求的是图片等等类型的文件
# 			with open('static' + request_path, 'rb') as file:
# 				# 读取文件数据
# 				file_data = file.read()
# 		except Exception as e:
#
# 			# 准备响应报文数据
# 			# 响应行
# 			response_line = 'HTTP/1.1 404 Not Found\r\n'
# 			# 响应头
# 			response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
# 			# 响应体
# 			response_body = '很抱歉,页面不存在'.encode()
#
# 			# 匹配响应报文数据
# 			response_data = (response_line + response_header + '\r\n').encode() + response_body
# 			server_client_socket.send(response_data)
# 		else:
# 			response_line = 'HTTP/1.1 200 OK\r\n'
# 			# 响应头
# 			response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
# 			# 响应体
# 			response_body = file_data
#
# 			# 匹配响应报文数据
# 			response_data = (response_line + response_header + '\r\n').encode() + response_body
# 			server_client_socket.send(response_data)
# 		finally:
# 			server_client_socket.close()
# def main():
# 	# 创建socket
# 	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	# 设置socket端口,立即释放端口
# 	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 	# 绑定端口号
# 	tcp_server_socket.bind(('', 9090))
# 	# 设置监听
# 	tcp_server_socket.listen(128)
# 	# 循环接收客户端的连接请求
# 	while True:
# 		# 等待客户端连接服务器
# 		server_client_socket, ip_port = tcp_server_socket.accept()
# 		# 开辟协程并执行对应的任务
# 		gevent.spawn(handle_client_request,server_client_socket)
#
# # 循环接收客户端的连接请求
#
# if __name__ == '__main__':
# 	main()
"""web服务器面向对象开发"""
# import socket
# import re
# import gevent
# from gevent import monkey
#
# monkey.patch_all()


# 封装的web服务器类
# class HttpWebServer:
# 	def __init__(self):
# 		# 创建socket
# 		tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 		# 设置socket端口,立即释放端口
# 		tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 		# 绑定端口号
# 		tcp_server_socket.bind(('', 9090))
# 		# 设置监听
# 		tcp_server_socket.listen(128)
# 		# 创建对象提供socket属性
# 		self.tcp_server_socket = tcp_server_socket
#
# 	def start(self):
# 		# 循环接收客户端的连接请求
# 		while True:
# 			# 等待客户端连接服务器
# 			server_client_socket, ip_port = self.tcp_server_socket.accept()
# 			# 开辟协程并执行对应的任务
# 			gevent.spawn(self.handle_client_request, server_client_socket)
#
# 	# 处理客户端的请求
# 	@staticmethod  # 方法里面不用实例对象和类对象,就写成静态方法
# 	def handle_client_request(server_client_socket):
# 		# 获取客户端请求的数据报文
# 		client_request_data = server_client_socket.recv(4096)
#
# 		client_request_content = client_request_data.decode()
# 		# 通过正则查找请求的资源路径
# 		match_obj = re.search(r'/\S*', client_request_content)
# 		# 判断路径匹配失败后的操作
#
# 		if not match_obj:
# 			print('访问路径有误')
# 			server_client_socket.close()
# 			return
#
# 		# 获取匹配结果
# 		request_path = match_obj.group()
# 		print(request_path)
#
# 		if request_path == '/':
# 			# 如果用户没有指定,据默认访问首页
# 			request_path = '/index.html'
#
# 		try:
# 			# 读取指定文件数据
# 			# 使用rb的原因是浏览器也有可能请求的是图片等等类型的文件
# 			with open('static' + request_path, 'rb') as file:
# 				# 读取文件数据
# 				file_data = file.read()
# 		except Exception as e:
#
# 			# 准备响应报文数据
# 			# 响应行
# 			response_line = 'HTTP/1.1 404 Not Found\r\n'
# 			# 响应头
# 			response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
# 			# 响应体
# 			response_body = '很抱歉,页面不存在'.encode()
#
# 			# 匹配响应报文数据
# 			response_data = (response_line + response_header + '\r\n').encode() + response_body
# 			server_client_socket.send(response_data)
# 		else:
# 			response_line = 'HTTP/1.1 200 OK\r\n'
# 			# 响应头
# 			response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
# 			# 响应体
# 			response_body = file_data
#
# 			# 匹配响应报文数据
# 			response_data = (response_line + response_header + '\r\n').encode() + response_body
# 			server_client_socket.send(response_data)
# 		finally:
# 			server_client_socket.close()
#
#
# def main():
# 	server = HttpWebServer()
# 	server.start()
#
# if __name__ == '__main__':
# 	main()

"""给web服务器加上命令行参数"""
import socket
import re
import gevent
from gevent import monkey
import sys

monkey.patch_all()


# 封装的web服务器类
class HttpWebServer:
	def __init__(self, port):
		# 创建socket
		tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 设置socket端口,立即释放端口
		tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
		# 绑定端口号
		tcp_server_socket.bind(('', port))
		# 设置监听
		tcp_server_socket.listen(128)
		# 创建对象提供socket属性
		self.tcp_server_socket = tcp_server_socket

	def start(self):
		# 循环接收客户端的连接请求
		while True:
			# 等待客户端连接服务器
			server_client_socket, ip_port = self.tcp_server_socket.accept()
			# 开辟协程并执行对应的任务
			gevent.spawn(self.handle_client_request, server_client_socket)

	# 处理客户端的请求
	@staticmethod  # 方法里面不用实例对象和类对象,就写成静态方法
	def handle_client_request(server_client_socket):
		# 获取客户端请求的数据报文
		client_request_data = server_client_socket.recv(4096)

		client_request_content = client_request_data.decode()
		# 通过正则查找请求的资源路径
		match_obj = re.search(r'/\S*', client_request_content)
		# 判断路径匹配失败后的操作

		if not match_obj:
			print('访问路径有误')
			server_client_socket.close()
			return

		# 获取匹配结果
		request_path = match_obj.group()
		print(request_path)

		if request_path == '/':
			# 如果用户没有指定,据默认访问首页
			request_path = '/index.html'

		try:
			# 读取指定文件数据
			# 使用rb的原因是浏览器也有可能请求的是图片等等类型的文件
			with open('static' + request_path, 'rb') as file:
				# 读取文件数据
				file_data = file.read()
		except Exception as e:

			# 准备响应报文数据
			# 响应行
			response_line = 'HTTP/1.1 404 Not Found\r\n'
			# 响应头
			response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
			# 响应体
			response_body = '很抱歉,页面不存在'.encode()

			# 匹配响应报文数据
			response_data = (response_line + response_header + '\r\n').encode() + response_body
			server_client_socket.send(response_data)
		else:
			response_line = 'HTTP/1.1 200 OK\r\n'
			# 响应头
			response_header = 'Server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
			# 响应体
			response_body = file_data

			# 匹配响应报文数据
			response_data = (response_line + response_header + '\r\n').encode() + response_body
			server_client_socket.send(response_data)
		finally:
			server_client_socket.close()


def main():
	print(sys.argv)
	if len(sys.argv) != 2:
		print('启动命令如下:Py-3 xxx.py 9090')
		return
	if not sys.argv[1].isdigit():
		print('启动命令如下:Py-3 xxx.py 9090')
		return
	port = int(sys.argv[1])
	print(port)

	server = HttpWebServer(port)
	server.start()


if __name__ == '__main__':
	main()
