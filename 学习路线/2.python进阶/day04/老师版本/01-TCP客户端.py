import socket


# 1 创建套接字              IPv4             流式报文
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 建立和服务器之间的连接 参数是服务器的IP地址和端口的元组
tcp_socket.connect(('192.168.14.100', 8080))


# 3 向服务器发送数据 参数是需要发送的数据<bytes类型>
data = input("请输入需要发送给服务器的数据:")
tcp_socket.send(data.encode())

# 4 阻塞等待地接收数据 参数是 本次接收到额最大字节  正常情况下返回值是接收到数据<bytes>
recv_data = tcp_socket.recv(1024)
print("接收到来自服务器的数据:%s" % recv_data.decode())

# 5 关闭套接字
tcp_socket.close()