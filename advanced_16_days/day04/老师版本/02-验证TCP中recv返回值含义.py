import socket


# 1 创建套接字              IPv4             流式报文
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 建立和服务器之间的连接 参数是服务器的IP地址和端口的元组
tcp_socket.connect(('172.16.51.134', 8080))

while True:
    # 3 向服务器发送数据 参数是需要发送的数据<bytes类型>
    data = input("请输入需要发送给服务器的数据:")
    tcp_socket.send(data.encode())

    # 4 阻塞等待地接收数据 参数是 本次接收到额最大字节  正常情况下返回值是接收到数据<bytes>
    # 如果对方断开连接  返回值就是b'' 是一个对方断开连接的标识 而不是对方发送过来的数据
    recv_data = tcp_socket.recv(1024)
    # recv_data  != None and recv_data != ''
    if recv_data:
        print("接收到来自服务器的数据:%s" % recv_data)
    # recv_data 为 None ''
    else:
        print("服务器断开连接了")
        break

# 5 关闭套接字
tcp_socket.close()