import socket

# 创建
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
tcp_socket.connect(('192.168.14.26', 8899))

# 获取文件名
file_name = input('输入文件名:')

# 编码,以便传输
file_name_data = file_name.encode('gbk')

# 发送数据
tcp_socket.send(file_name_data)

with open('F:/Python就业班/预习/客户端/' + file_name, 'wb') as file2:  # 这是客户端下载路径  file2是新的一个文件来装入接收到的数据流
	while True:
		# 接收服务器数据
		file_data = tcp_socket.recv(1024)
		if file_data:  # 如果file_data存在
			# 写入到指定文件
			file2.write(file_data)  # file2是一个新的空文件,拿来写入接收到的二进制数据
		else:
			break
# 关闭
tcp_socket.close()

# 注意: tcp服务端绑定端口号,程序退出后端口号不会立即释放,解决方法是设置socket
# 选项,让程序退出端口号后立即释放,也称为复用
