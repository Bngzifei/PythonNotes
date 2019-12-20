print('UDP...')
"""
IP地址:互联网协议地址,计算机的通行证.计算机在网络中的唯一身份标识.
桥接:Ubuntu虚拟机 直接连到局域网
NAT:网络地址转换
点分十进制:192.168.14.115
IP地址通常为4个字节,简称ipv4,这个.是形式上有的,实际的数据中没有这个.
IPv6:长度为8个字节

127.0.0.1:本地回环测试的地址,不能用作和其他计算机通信.

sudo ifconfig 网卡名 ip地址:设置ip地址

所有的手动设置的ip地址在重启之后都会失效

ifconfig:Ubuntu
ipconfig:Window


ping:和其他电脑之间通信是否正常

ping ip/域名:有正常返回

没有显示可能是通畅的,原因是对方的主机设置成了不回复类型.

端口:为什么是飞秋这个程序收到了而不是其他的程序?原因就是端口进行标识.

飞秋:2425端口

端口作用:用来标识计算机中的一个应用程序<服务>

ip + 端口:唯一确定网络中的一个程序,一般组合在一起使用,简称套接字地址.

数量:0-65535:一共65536个 两个字节标识的,是16个比特位,2bytes = 16 bit,2^16=65535 

知名端口:0-1023,一般没人用0端口.

1024-65535:动态端口

80:HTTP
22:SSH
21:FTP
443:HTTPS

netstat -an | grep ':8080'

lsof -i [tcp/udp]:8080



解决dpkg安装时候的锁问题:
# dpkg lock  sudo rm /var/lib/dpkg/lock && sudo dpkg --configure -a

"""

"""
udp:用户数据包协议

无连接:不管对方在不在线,只管发送.

只需要知道对方的地址即可

不可靠,易丢包.

socket:套接字,不同电脑之间不同程序之间的通信
实现不同进程之间的一种通信工具.

gram:报

dgram:数据报,data gram的简写就是dgram.
客户端和客户端之间无法通信.必须要服务器中转.

计算机中无法发送str类型数据,必须进行转换,转换成二进制类型数据才能进行发送

python3中:
str --> bytes :encode(),默认为utf-8编码,所以不用写参数默认是utf-8,可以省略不写
bytes ----> str : decode(),二进制解码为str

utf-8:一个汉字:3个字节
gbk:一个汉字2个字节


encode(encoding,errors): encoding -->指定编码方式,errors  --> 指定 如果编码解码

出错,strict:严格模式,抛出异常,ignore:忽略编码解码错误,宽松模式,会忽略异常.

Ubuntu 16.0 中默认是utf-8 编码

Window下的调试助手需要utf-8的编码,但是发送的时候是gbk编码
"""
"""
步骤:
1.>创建socket      udp_socket = socket.socket()
2.>发送消息        udp_socket.sendto()
3.>接收返回        udp_socket.recvfrom(1024)
4.>关闭socket      udp_socket.close()



"""
# while True:
import socket

# 1.创建套接字  地址协议族 ipv4 --> socket.AF_INET  套接字类型 用户数据报 -->socket.SOCK_DGRAM
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 接收方地址,在socket中这个是组合成一个元组类型来使用的
recv_addr = ('127.0.0.1', 8089)
data = input('输入要发送的数据:')

# 2.发送消息
# 使用sendto()发送数据,参数1是数据,参数2是目的地址(也叫接收地址(ip和端口)),原因是udp是无连接的,所以必须标识清楚发给谁,发的什么数据?
udp_socket.sendto(data.encode(), recv_addr)  # 记得给输入的字符串数据进行编码转成bytes类型,才能进行数据传输.

# 3.接收消息
# 返回值是一个元组类型,里面包括 发送的数据和发件地址(ip + 端口)  原因还是udp是无连接的,所以接收方也需要标识清楚发件方是谁,发的是什么.
# 接收使用recv.from()方法,参数是数据大小,一般设定为1024的整数倍即可.

# 因为不是面向连接的所以不知道是谁发过来的信息,所以返回值就需要有一个地址来标记是谁发过来的
recv_data, address = udp_socket.recvfrom(1024)  # 本次接收数据的最大长度,一般为1024的整数倍
print('接收到来自%s的数据:%s' % (address, recv_data.decode('GBK')))

# 4.关闭套接字
udp_socket.close()

# (数据bytes,(IP地址,端口)) = recvfrom(1024)  # 本次接收的最大字节
# bind((本地IP,端口))  申请固定端口,本地ip 一般设置为空
