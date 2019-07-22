def fib(n):
	num1, num2 = 1, 1
	count = 0
	while count < n:
		yield num1  # 可以返回多个值  yield 1,2,3
		count += 1
		num1, num2 = num2, num1 + num2
	return 1000


#  最后不需要raise StopIteration <生成器内部已经自动实现>
# 一般在生成器中不使用return关键字,一旦使用就会结束生成器的迭代过程
if __name__ == '__main__':
	f = fib(10)
	# for i in f:  可以取出多个值 for i,j in f:...
	# 	print(i)

	# 如果需要获取生成器函数的最终返回值,需要捕获迭代的异常
	# while True:
	# 	# 通过迭代器取出下一个元素的值<返回值>
	# 	try:
	# 		pass
	# 	except Exception as e:
	# 		print(e)
	# 		break
	# 	else:
	# 		print(i)

"""send()唤醒生成器,可以传参数"""
