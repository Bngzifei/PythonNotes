from socket import *

# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# # 2. 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
local_addr = ('', 7788)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udp_socket.bind(local_addr)

# 注意:只有先bind了才能进行sendto()操作.
udp_socket.sendto("hello".encode(), ('192.168.22.55', 8080))

udp_socket.close()
