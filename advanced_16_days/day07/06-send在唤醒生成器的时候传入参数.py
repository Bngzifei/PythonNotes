"""
面试问:
yield的作用:

send()可以传参数,不能第一次使用

使用场景:在生成下一个的时候,从我 指定的位置<传入的参数>开始生成
通过传入的参数,控制生成器下一次生成的元素

"""
"""
唤醒生成器:
元素的值=next(生成器对象)
元素的值=生成器.send(数据)

异同:
	next是函数  send()是方法
	next不能传参数,send可以传入参数<通过传输不同的参数控制生成器执行的逻辑>
	第一次只能next,其余地方随意使用<参数的值只有yield可以接收,因为第一次的时候没有yield>
同:
	获取到下一个元素的值<迭代>


yield关键字作用:
	1.挂起当前函数代码,将后面的表达式返回,调用生成器的地方
	2.接收可能存在的参数,紧接着上次执行的地方继续往下执行

"""


def fib(n):
	num1, num2 = 1, 1
	count = 0
	while count < n:
		# send()发送的消息只有yield关键字才能接收
		ret = yield num1
		print('接收到的参数是:', ret)
		count += 1
		num1, num2 = num2, num1 + num2


if __name__ == '__main__':
	f = fib(10)
	# 在第一次调用生成器的时候必须使用next(),因为第一次的时候没有yield接收传入的参数
	# TypeError: can't send non-None value to a just-started generator
	# 意思就是不能在第一次的时候将非None的数据发送给生成器.
	# print(f.send(None))  这样就可以
	print(next(f))
	print(f.send(101))
	print(f.send(102))
	print(f.send(103))
	print(f.send(103))
	print(f.send(103))


"""
容器类型就是典型的可迭代对象.

典型的:意思就是通用的,肯定是,具有代表性的

生成器肯定是可迭代对象.反之不行

"""