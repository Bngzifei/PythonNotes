"""光标在哪?类似于
文件的定位  会影响 读 和 取的 位置
都会改变文件的定位

"""

with open('123.txt', 'w+') as f:  # w+ 可读可写模式
	print(f.tell())
	f.write('hello')
	print(f.tell())

	"""
	offset:偏移,基于whence进行向后偏移字节
	一个字符就是占一个字节
	seek(offset,whence)
	whence:只能0:移动定位到文件开头,1,当前定位 2,移动到文件末尾
	"""
	f.seek(3, 0)  # 在Python3中offset和whence必须有一个是0,只能基于文件开头进行偏移,改进了是为了有意义
	content = f.read()  # 写完之后光标在字符串的最后,所以就读不出来了
	print(content)
