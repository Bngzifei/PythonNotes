"""
客户端:1.连接服务器(ip,port)
		2.下载文件的名字
服务器接收到客户端需要下载的文件名字,搜索文件,传给客户端
客户端写入到自己的文件中.


"""
# 1. 输入服务器ip,端口
# 2. 建立socket 连接服务器
# 3. 输入文件名
# 4. 发送文件名给服务器
# 5. 使用socket接收来自服务器的数据(保存在文件中)
# 6.如果收到b'',说明服务器断开连接-已经下载好
# 7.关闭socket


import socket

server_ip = input('输入server的ip:')
server_port = int(input('输入server的port:'))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

file_name = input('输入下载的文件名:')

client_socket.send(file_name.encode())

# 文本方式打开   str类型  需要解码  图片无法解码,所以直接使用二进制方式打开即可
with open("download" + file_name, 'wb') as file:
	while True:
		file_data = client_socket.recv(4096)  # ConnectionAbortedError: [WinError 10053] 你的主机中的软件中止了一个已建立的连接。原因是服务器出错了
		# 如果对方断开连接,我们就接收到b''
		if not file_data:
			print('服务器断开连接,说明文件传输完成')
			break

		# 否则就将收到的数据直接写入带文件中
		file.write(file_data)

client_socket.close()
