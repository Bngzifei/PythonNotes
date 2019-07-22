"""
授权:授权的过程是所有更新的功能都是由新的类的某部分来处理,但是,已经存在的功能就授权给对象,当做对象的默认属性.

理解:就是新的自己去造,原有的拿来直接使用.
实现授权的关键点是  覆盖__getattr__方法
也可以理解为授权也是一种包装
包装:是使用继承的方式实现的功能定制

工厂函数其实就是一个类,类有很多的方法

类似于一种权限管理
"""
"""需求:定制,修改一部分功能,不是全部"""

import time


class FileHandle:
	def __init__(self, filename, mode='r', encoding='utf-8'):
		# self.filename = filename  open() 操作打开的是一个文件句柄
		# 调用系统提供的open()方法
		self.file = open(filename, mode, encoding=encoding)
		self.mode = mode
		self.encoding = encoding
	
	def write(self, line):
		# print('*' * 30, line)
		# Y- year, m- month d- day X- 就是时分秒三个合起来了.
		t = time.strftime('%Y-%m-%d %X')
		self.file.write('%s %s' % (t, line))
	
	def __getattr__(self, item):
		# print(item, type(item))  # item就是执行的那个方法,<class 'str'>
		# self.file.read()
		return getattr(self.file, item)  # 通过字符串获取自己的方法,属性


f1 = FileHandle('a.txt', 'r+')
print(f1.file)  # <_io.TextIOWrapper name='a.txt' mode='r+' encoding='utf-8'>
print(
	f1.__dict__)  # {'file': <_io.TextIOWrapper name='a.txt' mode='r+' encoding='utf-8'>, 'mode': 'r+', 'encoding': 'utf-8'}

print(f1.read)  # 找不到就触发__getattr__()
# <built-in method read of _io.TextIOWrapper object at 0x0000025619768B40> 内存地址

sys_f = open('b.txt', 'w+')
print('-->', getattr(sys_f, 'read'))
# <built-in method read of _io.TextIOWrapper object at 0x000002D37B7C8C18>
f1.read()


# f1.write('111111111119\n')  # 写入数据
# f1.write('cpu负载过高\n')
# f1.write('内存剩余不足\n')
# f1.write('硬盘剩余不足\n')
# f1.seek(0)  # 将读取光标移动到开始位置
# # print(f1.seek(0))  # 0
# print(f1.read())  # 可以读出来
