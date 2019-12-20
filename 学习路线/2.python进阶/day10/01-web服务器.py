"""
流程: Nginx  脑海中建立一条生产线
PWS1.0目的:在用户每次访问的时候,都返回一个固定的数据,例如Hello World
1.>接收请求报文
2.>解析请求报文-得到用户需求
3.>根据用户的需求找到对应的资源
4.>资源打包到HTTP响应报文
5.>发送响应报文给浏览器

最开始肯定是最简单的,一步一步的加多,慢慢地才会出来
PWS1.0:Python Web Server 1.0
"""
import socket


def main():
	# 1. 创建tcp服务器的socket  设置选项 绑定 监听
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(('', 8887))  # 这里绑定的是服务器的固定端口,目的是让客户端能连接到了我的机器上面之后,可以找到我的这个程序
	server_socket.listen(128)

	while True:
		# 2.接受用户连接,从这里开始才是需要不断的进行,才使用死循环
		client_socket, client_addr = server_socket.accept()
		print('接受到%s的连接请求' % str(client_addr))

		# 3.接收用户请求报文
		request_data = client_socket.recv(4096)
		print(type(request_data))  # <class 'bytes'>
		print(request_data)

		# 4.返回固定的数据 Hello World  打包到响应报文中   PWS1.0\r\n这里是一个空行\r\n  所以不能少   <h1> 标题加粗的效果
		#               响应行               响应头/可以是0个  空行<不能省略,隔离作用> 响应体数据   这四个 只有响应头可以省略,其他的都不可以省略
		response_data = 'HTTP/1.1 200 OK\r\nServer:PWS1.0\r\n\r\n' + '<h1>Hello World</h1>'
		client_socket.send(response_data.encode())

		# 5.一次请求/响应 就关闭连接  --> 短连接
		client_socket.close()


if __name__ == '__main__':
	main()
