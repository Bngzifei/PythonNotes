import socket

r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dest_addr = ('192.168.14.121', 8080)

send_data = input('发送的数据:')

r.sendto(send_data.encode('utf-8'), dest_addr)

recv_data = r.recv(1024)  # 1024表示本次接收的最大字节数

print(recv_data[0].decode('gbk'))  # 数据
print(recv_data[1])  # ip和端口

r.close()
