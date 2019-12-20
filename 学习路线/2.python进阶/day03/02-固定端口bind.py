import socket

# 1 创建套接字            地址协议族ＩＰｖ４　套接字类型 用户数据报
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# 使用固定端口 绑定 IP地址,填空代表使用本机的任意IP ,因为一般来说一台主机的IP不止一个,有外网ip和内网ip,还有一个127.0.0.1本地ip.
udp_socket.bind(('', 8888))

# 2 发送消息
data = "你好,吃饭了吗"
recv_address = ('192.168.14.114', 8080)

# 参数１是需要发送的数据－bytes　目的地址IP<字符串>和端口<数字>
udp_socket.sendto(data.encode(), recv_address)

# 3 接收消息 参数１是本次接收的数据的最大长度
# 返回值　　(b'abcd', ('192.168.14.114', 8080))
# 返回值是　数据　发件人地址构成的元组
recv_data, remote_address= udp_socket.recvfrom(1024)

print("接收到来自%s的数据:%s" % (recv_address, recv_data.decode()))

# 4 关闭套接字
udp_socket.close()