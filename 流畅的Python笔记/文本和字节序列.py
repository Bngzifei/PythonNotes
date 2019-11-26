"""
人类使用文本,计算机使用字节序列


Python3明确区分了人类可读的文本字符串和原始的字节序列.隐式地把字节序列转换成Unicode文本已
成过去.


说到底,本章涵盖的问题对只处理ASCII文本的程序员没有影响.



字符问题:
	
	字符串是个相当简单的概念:一个字符串是一个字符序列.问题出现在"字符"的定义上.

	在2015年,"字符"的最佳定义是Unicode字符.因此,从Python3的str对象中获取的元素是Unicode字符.
	这相当于从Python2的unicode对象中获取的元素.而不是从Python2的str对象中获取的原始字节序列.

编码是在码位和字节序列之间转换时使用的算法.

把码位转换成字节序列的过程是编码,把字节序列转换成码位的过程是解码.

如果想帮助自己记住.decode()和.encode()的区别,可以把字节序列想成晦涩难懂的机器磁芯转储,把Unicode字符串
想成"人类可读"的文本.那么,把字节序列变成人类可读的文本字符串就是解码,而把字符串变成用于存储或者传输的字节序列
就是编码.

虽然Python3的str类型基本相当于Python2的unicode类型,只不过是换了个新名称.但是Python3的bytes类型却不是把str类
型转个名称那么简单,而且还有关系紧密的bytearray类型.因此,在讨论编码和解码的问题之前,有必要先来介绍一下二进制序列
类型.


字节概要:
	
	新的二进制序列类型在很多方面与Python2的str类型不同,首先要知道,Python内置了两种基本的二进制序列类型:Python3引入
	的不可变bytes类型和Python2.6添加的可变bytearray类型.(Python2.6也引入了bytes类型,但那只不过是str类型的别名,与
	Python3的bytes类型不同)

	bytes或bytearray对象的各个元素是介于0~255(含)之间的整数,而不像Python2的str对象那样是单个的字符.然而,二进制序列
	的切片始终是同一类型的二进制序列,包括长度为1的切片.

"""


# 包含5个字节的bytes和bytearray对象
cafe = bytes("cafe",encoding="utf_8")   # bytes对象可以从str对象使用给定的编码构建
print(cafe)  # b'cafe'
print(cafe[0])  # 99  各个元素是range(256)内的整数
print(cafe[:1])  # b'c'  bytes对象的切片还是bytes对象即使是只有一个子节的切片

print("=====================>>>")

cafe_arr = bytearray(cafe)
print(cafe_arr)  # bytearray(b'cafe')  bytearray对象没有字面量句法,而是以bytearray()和字节序列字面量参数的形式显示.
print(cafe_arr[-1:])  # bytearray(b'e')  bytearray对象的切片还是bytearray对象

"""
my_bytes[0]获取的是一个整数,而my_bytes[:-1]返回的是一个长度为1的bytes对象----这一点应该不会让人意外.s[0] == s[:1]只对str
这个序列类型成立.不过,str类型的这个行为十分罕见.对其他各个序列类型来说,s[i]返回一个元素,而s[i:i+1]返回一个相同类型的序列,
里面是s[i]元素.


虽然二进制序列其实是整数序列,但是它们的字面量表示法表明其中有ASCII文本.

	可打印的ASCII范围内的字节(从空格到~),使用ASCII字符本身.

	制表符,换行符,回车符,和\对应的字节,使用转义序列\t,\n,\r和\\

	其他字节的值,使用十六进制转义序列(例如,\x00是空字节)


二进制序列有个类方法是str没有的,名为fromhex,它的作用是解析十六进制数字对(数字之间的空格是可选的),构建二进制序列:
>>>bytes.fromhex("31 4B CE A9")
b"1K\xce\xa9"


构建bytes或bytearray实例还可以调用各自的构造方法,传入下面的参数:

	一个str对象和一个encoding关键字参数

	一个可迭代对象,提供0~255之间的数值

	一个整数,使用空字节创建对应长度的二进制序列.

	一个实现了缓冲协议的对象(如bytes,bytearray,memoryview,array.array);此时,把源对象中的字节序列复制到新建的二进制序列中.

缓冲协议:https://docs.python.org/zh-cn/3/c-api/buffer.html#bufferobjects


使用缓冲类对象构建二进制序列是一种低层操作,可能涉及类型转换.

"""

# 使用数组中的原始数据初始化bytes对象
import array
numbers = array.array("h",[-2,-1,0,1,2])
octets = bytes(numbers)
print(octets)  # b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'

"""
使用缓冲类对象创建bytes或bytearray对象时,始终复制源对象中的字节序列.与之相反,memoryview对象允许在二进制数据结构之间共享内存.
如果想从二进制序列中提取结构化信息,struct模块是重要的工具.


结构体和内存视图

	struct模块提供了一些函数,把打包的字节序列转换成不同类型的字段组成的元组,还有一些函数用于执行反向转换,把元组转换成打包的字节序列.
	struct模块能处理bytes,bytearray和memoryview对象.

	memoryview类不是用于创建或存储字节序列的,而是共享内存,让你访问其他二进制序列,打包的数组和缓冲中的数据切片,而无需复制字节序列,例如
	PIL就是这样处理图像的.



"""

# 使用memoryview和struct提取一个GIF图像的宽度和高度

import struct
fmt = "<3s3sHH"  # 结构体格式:<是小字节序,3s3s是两个3字节序列,HH是两个16位二进制整数
with open("filter.gif","rb") as fp:
	img = memoryview(fp.read())  # 使用内存中的文件内容创建一个memoryview对象

header = img[:10]  # 然后使用它的切片再创建一个memoryview对象;这里不会复制字节序列
print(bytes(header))  # 转换成字节序列,这只是为了显示,这里复制了10字节

struct.unpack(fmt,header)  # 拆包memoryview对象,得到一个元组,包含类型,版本,宽度和高度.
del header  # 删除引用,释放memoryview实例所占的内存
del img

"""
注意,memoryview对象的切片是一个新的memoryview对象,而且不会复制字节序列.

了解编解码问题

	UnicodeEncodeError（把字符串转换成二进制序列时）
	或 UnicodeDecodeError（把二进制序列转换成字符串时）。如果源码
	的编码与预期不符，加载 Python 模块时还可能抛出 SyntaxError。

	utf_?(比如utf-8,utf-16)能处理任何字符串

	error='ignore' 处理方式悄无声息地跳过无法编码的字符；这样做
    通常很是不妥。

    编码时指定 error='replace'，把无法编码的字符替换成 '?'；数
    据损坏了，但是用户知道出了问题。

    'xmlcharrefreplace' 把无法编码的字符替换成 XML实体.


使用预期之外的编码加载模块时抛出的SyntaxError
	
	Python3默认使用utf-8源码编码,Python2(从2.5开始)则默认使用ASCII.如果加载的.py模块中
	包含utf-8之外的数据,而且没有声明编码,会得到类似下面的消息:

	SyntaxError: Non-UTF-8 code starting with '\xe1' in file ola.py on line
    1, but no encoding declared; see http://python.org/dev/peps/pep-0263/
    for details


    现在,Python3的源码不再限于使用ASCII,而是默认使用优秀的utf-8编码,因此要修正源码的陈旧编码问题,
    最好将其转换成utf-8,别去麻烦coding注释.

    Python3允许在源码中使用费ASCII标识符.

选择对团队而言易于阅读的人类语言,然后使用正确的字符拼写.



如何找出字节序列的编码?
	
	假如有个文本文件,里面保存的是源码或者诗句,但是你不知道它的编码.那么如何查明真的的编码呢?

	简单来说,不能.必须有人告诉你.

	然而,就像人类语言也有规则和限制一样,只要假定字节流是人类可读的纯文本,就可能通过试探和分析找出编码.

	例如:如果b"\x00"字节经常出现,那么可能是16位或者32位编码,而不是8位编码方案,因为纯文本中不能包含空字符.
	如果字节序列b"\x20\x00"经常出现,那么可能是utf-16le编码中的空格字符.

统一字符编码侦测包Chardet就是这样工作的,它能识别所支持的30种编码.Chardet是一个Python库,可以在程序中使用.

二进制序列编码文本通常不会明确指明自己的编码,但是utf格式可以在文本内容的开头添加一个字节标记.


BOM:有用的鬼符

	>>> u16 = 'El Niño'.encode('utf_16')
	>>> u16
	b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'

	我指的是 b'\xff\xfe' .这是BOM,即字节序标记(byte-order-mark),指明编码时使用IntelCPU的小字节序.

需要在多台设备中或多种场合下运行的代码,一定不能依赖默认编码.打开文件时始终应该明确传入 encoding=参数,因为不同的
设备使用的默认编码可能不同,有时隔一天也会发生变化.



	




















	


"""





































