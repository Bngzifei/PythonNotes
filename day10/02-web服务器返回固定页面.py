"""
PWS2.0目的:在用户每次访问的时候,都会返回一个固定的页面,比如index.html

1.>接收请求报文
2.>解析请求报文-得到用户需求
3.>根据用户的需求找到对应的资源
4.>资源打包到HTTP响应报文

最开始肯定是最简单的,一步一步的加多,慢慢地才会出来
PWS2.0:Python Web Server 2.0
"""
import socket


def main():
	# 1. 创建tcp服务器的socket  设置选项 绑定 监听
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(('', 8888))  # 这里绑定的是服务器的固定端口,目的是让客户端能连接到了我的机器上面之后,可以找到我的这个程序
	server_socket.listen(128)

	while True:
		# 2.接受用户连接
		client_socket, client_addr = server_socket.accept()
		print('接受到%s的连接请求' % str(client_addr))

		# 3.接收用户请求报文
		request_data = client_socket.recv(4096)
		print(request_data)

		# 4.返回固定的文件数据作为响应体   打包到响应报文中

		with open('33.jpg', 'rb') as file:
			html_data = file.read()  # html_data 是二进制bytes字节类型的数据

		# .encode()先把前面的str类型转成bytes字节类型,然后拼接
		response_data = ('HTTP/1.1 200 OK\r\nServer:PWS2.0\r\n\r\n').encode() + html_data
		client_socket.send(response_data)

		# 5.一次请求/响应 就关闭连接  --> 短连接
		client_socket.close()


if __name__ == '__main__':
	main()
