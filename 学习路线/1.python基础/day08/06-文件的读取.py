# with open('123.txt') as f:
# 	content = f.read(3)  # 3代表读取指定的字符 默认把文件中的内容全部读取
# # 快捷键跳到行首或行尾
# 	print(content)


# with open('123.txt') as f:
# 	content = f.readlines()  # 默认全部读取,返回一个列表,每一行是一个元素
# 	# 快捷键跳到行首或行尾
# 	print(content)


# 敲一个enter回车键就是一个\n

# 大文件读取要一点一点去读取,为了效率,省内存,提高效率
with open('123.txt') as f:
	while True:  # 一行读完就释放内存
		content = f.readline()  # 一次只读一行
		print(content, end='')  # print()默认是换行了,所以加end=''去掉换行效果
		if len(content) == 0:
			break
