import socket
import re
import gevent
from gevent import monkey
import sys

monkey.patch_all()  # 自动切换  time.sleep recv accept 这些类型的函数在执行的时候会出现大量的耗时等待,所以让这部分闲置时间加以利用.


class HTTPServer:
	"""web服务"""
	def __init__(self, port):
		"""初始化操作"""
		# 1. 创建tcp服务器的socket  设置选项 绑定 监听
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server_socket.bind(('', port))  # 这里绑定的是服务器的固定端口,目的是让客户端能连接到了我的机器上面之后,可以找到我的这个程序
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

	def client_handler(self, client_socket):
		"""处理每个客户端的请求"""
		# 3.接收用户请求报文
		request_data = client_socket.recv(4096)
		# 解码 bytes  --> str
		request_data_str = request_data.decode()
		print(request_data)
		# ps:当用户的请求路径为/时候,表示其请求的是首页 homepage
		# 解析用户请求 获取到用户的资源请求路径
		# 正则匹配 只要是有/ 提取请求路径
		# GET /index.html
		result = re.search(r'^\w+ (/\S*)', request_data_str)
		# 判断是否提取成功  成功就取出这个值,不成功结束程序
		if not result:  # 路径为空
			print('请求报文格式错误')
			client_socket.close()
			# 结束 这种情况
			return

		# 尽量扁平结构 不要使用else缩进去,那样的是嵌套结构,这是小技巧
		# 获取请求路径  资源路径<static> + /index.html
		# 如果执行到这里,一定是匹配成功了,因为失败的已经跳过了
		path_info = result.group(1)

		# 4.返回用户指定的文件数据作为响应体   打包到响应报文中  static + /index.html
		# static 是文件夹,open打不开 潜规则 :所有的web服务器 不写路径默认是主页

		# 如果path_info 是/,返回 index首页
		if path_info == '/':
			path_info = '/index.html'
# ---------------------------动态资源请求-------------------------->
		# 如果是动态资源,需要调用框架来处理  python中.html结尾的就是动态资源
		env = {
			'PATH_INFO': path_info  # 实际情况下web服务器会将所有的请求信息放到字典中,env是字典类型参数
		}
		if path_info.endswith('.html'):
			import Application

			status, headers, response_body = Application.app(env)
			# 先拼接响应行
			response_line = 'HTTP/1.1 %s\r\n' % status
			response_header = ''
			for name, value in headers:
				response_header += '%s:%s\r\n' % (name, value)
			response_data = response_line + response_header + '\r\n' + response_body
			client_socket.send(response_data.encode())
			client_socket.close()
# -------------------------静态资源的处理----------------------->
		else:
			# 静态资源的处理
			try:
				with open('static' + path_info, 'rb') as file:
					html_data = file.read()  # html_data 是二进制bytes字节类型的数据
			except Exception as e:
				with open('static/404.html', 'rb') as file:
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


def main():
	# 获取程序运行所需的参数<端口>   python3  1.py  8080  argv:['x.py',8080]
	if len(sys.argv) < 2:
		print('参数使用出错,应该是形如:python3 07-web服务器-命令行参数控制内部绑定的端口.py 8080')
	# 端口号是一个数字
	port = int(sys.argv[1])

	# 创建web服务
	http_server = HTTPServer(port)
	# 启动web服务
	http_server.start()


if __name__ == '__main__':
	main()
