"""
tcp:传输控制协议

步骤:1.创建连接 2.数据传送 3.终止连接

特点: 面向连接,可靠,基于字节流的传输层通信协议

应用场景:连接是一对一的,不适用于广播的应用程序.


可靠传输:
1.> 采用发送应答机制: 即发送的每个报文段必须的到对方的应答才认为这个tcp
报文段发送成功.

2.> 超时重传: 发送端发出一个报文之后会启动定时器,如果在定时时间内没有收到应答就重新发送这个报文段

为了保证不丢包,给每个报文编号,同时这个编号也保证了传送到接收端接收数据的有序接收.
接收端对已经接收的数据包发回给发送端一个确认信号(ACK);如果发送端在合理的往返时延内未收到确认,那么对应
的数据包就被假设为丢失,发送端会重传.

3.> 错误校验: 由发送端计算,然后由接收端验证,其目的是为了检测数据在发送端到接收端
之间的过程中是否有改动.如果接收端检测到校验有差错.则直接丢弃 这个数据包.

4.> 流量控制和阻塞管理: 流量控制用来避免主机发送数据过快而使得接收方来不及完全接收.

优点: 可靠.稳定
缺点: 传输速度慢 占用资源高


区别:

1.> tcp 面向连接,udp 不是面向连接
2.> tcp 可靠 udp 不可靠
3.> tcp传输速度慢  udp 传输快
4.> tcp 不支持广播 udp 支持广播
5.> tcp 占用资源多 udp 占用少
6.> tcp 适合发送大量数据 udp 适合少数据
7.> tcp 有流量控制 udp 没有流量控制


tcp 应用场景: 准确无误的传输数据
HTTP,HTTPS,FTP,POP,SMTP 协议



"""

"""tcp客户端:"""

# import socket
#
# # 创建socket对象            ipv4类型         tcp的socket类型是STREAM型
# tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # ip 端口设置
# server_ip = '192.168.14.26'
# server_port = 8088
#
# # 建立连接 connect()  记得参数类型是一个元组
# tcp_socket.connect((server_ip, server_port))
#
# send_data = input('发送数据是:')
#
# # send() 发送数据 ,参数是数据,记得数据是字符串类型,在传输的时候需要进行编码变成二进制流
# tcp_socket.send(send_data.encode('gbk'))
#
# # recv()接收服务器返回的数据,参数是1024的整数倍即可
# recv_data = tcp_socket.recv(1024)
#
#
# # 接收到的数据是二进制类型,需要解码才能看到str字符类型的数据.
# print('接收到的数据是:%s' % recv_data.decode('gbk'))
#
# # 记得关闭
# tcp_socket.close()



"""tcp 服务器:"""
# import socket
# # 创建socket
# tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# # 绑定本机
# tcp_server.bind(('', 8899))
# # 设置监听,因为是服务器所以是需要接收别人发送来数据,面向连接,所以需要监听发送端
# tcp_server.listen(5)  # 设置参数128来表示最大等待连接数,就是我服务器等你128次,128之后认为你这个数据发送失败,返回给发送端ack消息
# print('----1----')
# # 监听完了就是接收客户端的socket 和 地址
#
# # 如果有新的客户端来请求链接服务器,那么就产生一个新的socket专门为这个客户端服务
# # client_socket 用来为这个客户端服务
# # server就可以省下来专门等待其他新的客户端的链接
# client_socket, client_Info = tcp_server.accept()
# print('----2----')
#
# # 接收数据,是客户端产生的,所以使用client_socket去接收recv
# recv_data = client_socket.recv(1024)
# print('接收到的数据是:%s' % recv_data.decode('gbk'))
#
# # 给客户端发送一些数据,使用这个client_socket返回给客户端数据
# client_socket.send('hello'.encode('gbk'))
#
# # 关闭为这个客户端服务的socket,只要关闭了,就意味着不能再为这个客户端服务了如果还需要服务,只能再次重新连接
# client_socket.close()
# tcp_server.close()



"""另一个版本:"""
import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(("", 8899))

serverSocket.listen(5)

print("-----1-----")
clientSocket,clientInfo = serverSocket.accept()  # 服务器返回一个socket来服务客户端,accept()返回的是一个元组类型,(socket,客户端的信息),其中客户端信息就是ip地址和端口号,也是一个元组类型(ip,port)

print("-----2-----")
#clientSocket 表示这个新的客户端
#clientInfo 表示这个新的客户端的ip以及port

recvData = clientSocket.recv(1024)

print("-----3-----")
print("%s:%s"%(str(clientInfo), recvData.decode('gbk')))

clientSocket.close()
serverSocket.close()


"""tcp注意点:

1.> tcp服务器都需要绑定端口,否则客户端找不到这个服务器
2.> tcp客户端不需要绑定端口,使用随机端口即可
3.> tcp服务器使用listen()将socket 的主动变为被动,服务器必做的
4.> tcp的客户端和服务器 建立好连接才能收发数据
5.> tcp客户端和服务器连接成功后,服务器会有一个新的socket来专门标记这个客户端,单独为这个客户端服务
6.> listen之后的socket 是被动的,用来接收新的客户端的连接请求.
7.> accept返回的socket 是用来标记这个新的客户端的
8.> 关闭listen后的socket就说明被动的socket关闭了.会导致新的客户端无法连接服务器,但是之前已经连接成功的客户端能够正常通信.
9.> 关闭accept返回的socket就意味着这个客户端已经服务完毕
10.> 当客户端的socket调用close之后,服务器会recv阻塞,并且返回的长度为0,因此,服务器可以通过返回数据的长度来区别客户端是否已经下线.
















"""

