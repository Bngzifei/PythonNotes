print('tcp....')
"""
tcp:tcp使用较多.直接使用较少,使用  封装之后上层的库  较多.  不会有人从头开始写一个tcp的协议,
然后做个什么软件的,造轮子这事情,差不多就得了.知道原理,会使用别人造的库就行.出错了能够找到错误的原因,处理掉就好.

面试常问:tcp和udp的区别

tcp:Transmission Control Protocol  传输控制协议 

1.>面向连接(就是打电话的时候先拨号的操作)2.>可靠的(ACK应答)3.>基于字节流 stream的方式

面向连接:在通信之前确认双方在线.--> 在通信之前需要先建立连接<拨号>

字节流:无界限,没有量词来界定这个消息的体量,都是连接在一起的.
没有消息边界,对方多次发送的消息,我一次就接收.不是每次都接收一部分.从接收的数据中看不到数据是哪一次发送的.  简称tcp的 "粘包" 问题.

特点:面向连接,可靠,基于字节流

优点:可靠,稳定

缺点:慢,占用系统资源高

步骤:创建连接,数据传送,

不适用广播,一对一的单播

为啥可靠?原因:
	1.>发送应答:每发一次都必须得到对方的应答(ACK)
	
	2.>超时重传:一定的时间内没有收到回复,就认为这个数据包已经出错或者丢失,发送方会再次发这个数据包
	
	3.>错误校验:奇偶校验,循环冗余校验等等
	
	4.>流量控制与阻塞管理:发送方有一个动态调整的发送速度的机制.
	
	5.>有序编号
	
udp中无序,可能重复,有可能乱序.

最大特点有了connect()方法


socket就是一个手机,这么理解即可

1.创建socket(买个手机)
2.建立连接(拨号)
3.发送数据(通话)
4.关闭socket(挂掉)
"""