"""
服务器:
# 1. 创建服务器socket
# 2. bind() listen
# 3. 接受客户端连接请求,取出一个客户端关联的socket
# 4. 使用关联的socket和客户端进行通信
#    收客户端需要下载的文件名,发送文件名对应的数据
# 5. 发送完成,断开连接<就是关闭了client_socket
# 关闭服务器socket


"""


import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置选项  SO_REUSEADDR:二次利用,释放地址,重新利用地址
# 忽略2msl等待时间,直接进行这个地址的再次利用
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 9991))
server_socket.listen(128)

while True:
	client_socket, client_info = server_socket.accept()
	# print('接收到连接请求%s' % client_info)  #  TypeError: not all arguments converted during string formatting
	# print('接收到%s连接请求' % str(client_info))  # 记得这里的client_info是一个元组类型,不能使用%号来连接,客户端那边也会报错
	print('接收到连接请求:', client_info)  # 记得这里的client_info是一个元组类型,不能使用%号来连接,客户端那边也会报错

	file_name = client_socket.recv(256).decode()  # 文件名一般很短,256字节长度可以了

	# 打开本地文件,读取数据
	try:
		# 捕获如果没有这个文件的异常
		file = open(file_name, 'rb')
	except Exception as e:
		pass
	else:
		# 读取
		file_data = file.read()
		# 发送
		client_socket.send(file_data)
		# 关闭文件
		file.close()
	finally:
		# 关闭socket
		client_socket.close()

server_socket.close()
