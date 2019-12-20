"""
功能需求
文件下载器客户端程序发送下载请求的文件名给服务器
服务器接收到文件名，根据文件名读取文件数据，然后发送给客户端
客户端接收服务端发送的文件数据，然后写入到指定文件
"""

import socket
import os

# 创建 server_socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置选项  SO_REUSEADDR:二次利用,释放地址,重新利用地址
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定地址
server_socket.bind(('', 8899))

# 设置监听
server_socket.listen(5)

# 循环接收客户端请求

while True:

	# 接收客户端请求,分配socket处理
	service_socket, client_info = server_socket.accept()
	# 分配的socket接收客户端数据
	file_data = service_socket.recv(1024)
	# 解码接收到的二进制数据
	file = file_data.decode('gbk')
	# 输出解码后的数据
	print(file)
	# 输出客户端信息(ip,port)
	print(client_info)

	if os.path.exists(file):
		# 文件存在
		with open(file, 'rb') as file1:
			# 读取文件数据
			while True:
				file_data1 = file1.read(1024)
				# 读取成功,发送给客户端
				if file_data1:
					service_socket.send(file_data1)
				else:
					break
	else:
		print('文件不存在')

	# 终止和客户端的连接
	service_socket.close()

# 终止服务器的socket
server_socket.close()
