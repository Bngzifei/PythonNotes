if __name__ == '__main__':
	data = [1, 2, 3, 4, 5]
	# for i in data:
	# 	print(i)

	# 模拟for 遍历的  过程
	# 1.取出迭代器
	it = iter(data)  # 每次都是取出第一个元素
	while True:
		# 通过迭代器取出下一个元素的值<返回值>
		try:
			# it = iter(data)  # 每次都是取出第一个元素,不能放在这里,否则就是死循环.
			i = next(it)  # 迭代器的返回值赋给i
		# 如果迭代完成,则抛出StopIteration异常
		except Exception as e:
			print(e)
			break
		else:
			print(i)
