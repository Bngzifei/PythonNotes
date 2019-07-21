import socket


# 1 创建服务器套接字＜接受客户端的连接请求的套接字＞
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2 绑定端口
server_socket.bind(('', 8888))
# 3 安装客户服务系统－> 将套接字设置为被动套接字<被动接受连接　默认主动>; 设置等待服务区的大小
server_socket.listen(128)

while True:
    # 4 从等待服务区取出一个客户端用以服务　---＞　接受一个客户端连接
    # 返回值是一个元组　有两个元素　结构: (客户端套接字对象<分机>, (客户端ＩＰ，　端口))
    client_socket, client_addr = server_socket.accept()
    print("接受到来自%s的连接请求" % str(client_addr))

    while True:
        # 5 使用分机和和客户端进行交流　－　数据收发 收到的数据为非空表示数据; 其他表示客户端断开连接
        recv_data = client_socket.recv(1024)

        client_socket.send(recv_data)
        if recv_data:
            print("接收数据: %s" % recv_data.decode())
        else:
            print("客户端下线了")
            break
    # 6 关闭客户端套接字
    client_socket.close()
# # 7 关闭服务器套接字
# server_socket.close()