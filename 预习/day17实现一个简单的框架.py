import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()
import sys


class HttpWebServer:
	"""封装的web框架"""

	def __init__(self, port):
		# 创建tcp服务端socket
		tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 设置socket选项,立即释放端口
		tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# 绑定端口
		tcp_server_socket.bind(('', port))
		# 设置监听
		tcp_server_socket.listen(128)
		# 创建对象提供soxket属性
		self.tcp_server_socket = tcp_server_socket

	# 启动服务器
	def start(self):
		# 循环接收客户端的连接请求
		while True:
			service_client_socket, ip_port = self.tcp_server_socket.accept()
			# 开辟协程并执行相应的任务
			gevent.spawn(self.handle_client_request,service_client_socket)

	# 处理客户端的请求
	def handle_client_request(self, service_client_socket):
		# 获取客户端的请求报文数据
		client_request_data = service_client_socket.recv(4096)
		print(client_request_data)

		client_request_conent = client_request_data.decode('utf-8')
		# 通过正则查找请求的资源路径
		match_obj = re.search(r'\S*', client_request_conent)
		if not match_obj:
			print('访问路径有误')
			service_client_socket.close()
			return
		# 获取匹配结果
		request_path = match_obj.group()
		print(request_path)

		if request_path == '/':
			# 如果用户没有指定资源路径,那么默认访问的数据是首页的数据
			request_path = '/index.html'
		if request_path.endswith('.html'):
			# 判断用户的请求路径 是否以.html结尾的 是--> 动态资源请求
			env = {
				'PATH_INFO': request_path
			}

			import Application
			# app返回值就是响应状态,响应头,响应体
			status, headers, response_body = Application.app(env)
			response_data = 'HTTP/1.1 %s\r\n' % status
			for header in headers:
				response_data += '%s: %s\r\n' % header
			response_data = response_data + '\r\n' + response_body
			service_client_socket.send(response_data.encode())
			service_client_socket.close()
		else:
			# 读取指定文件数据
			# 使用rb的原因是浏览器请求的数据也有可能是音频,图片等
			try:
				with open('static' + request_path, 'rb') as file:
					# 读取文件数据
					file_data = file.read()
			except Exception as e:
				# 准备响应报文数据
				# 响应行
				response_line = 'HTTP/1.1 404 Not Found\r\n'
				# 响应头
				response_header = 'Server:PWS1.0\r\nContent-Type:text/html;charset=utf-8\r\n'
				# 响应体 -> 打开一个404html数据给浏览器
				response_body = '<h1>非常抱歉,您访问的网页已经不存在了</h1>'.encode('utf-8')
				# 匹配响应报文数据
				response_data = (response_line + response_header + '\r\n').encode('utf-8')
				# 发送响应报文数据
				service_client_socket.send(response_data)
			else:
				# 响应行
				response_line = 'HTTP/1.1 200 OK\r\n'
				# 响应头
				response_header = 'Server:PWS1.0\r\nContent-Type:text/html;charset=utf-8\r\n'
				# 响应体
				response_body = file_data
				# 匹配响应报文数据
				response_data = (response_line + response_header + '\r\n').encode('utf-8') + response_body
				# 发送响应报文数据
				service_client_socket.send(response_data)
			finally:
				service_client_socket.close()


def main():
	"""主函数"""
	print(sys.argv)
	if len(sys.argv) != 2:
		print('启动命令如下:python3 xxx.py 9090')
		return
	if not sys.argv[1].isdigit():
		print('启动命令如下:python3 xxx.py 9090')
		return
	port = int(sys.argv[1])
	server = HttpWebServer(port)
	server.start()


if __name__ == '__main__':
	main()
