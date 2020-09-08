"""
当try里面的代码出错后,try内部后续待吗不会执行,而是直接执行对应的except里面的代码.


如果try里面的代码出错后,默认应该由当前try对应的except去拦截,如果拦截住,就相当于异常已经消失,如果当前try后面的except无法拦截异常,这个异常就会向外层的try传递,由外层对应的except去拦截.以此类推.一直到Python解释器为止.


异常只会向外层传递,不会向内层传递.(在函数嵌套和try嵌套里面都是这个顺序.)

"""

try:
	f = open('13.txt', 'r')  # 一出错就立刻跳到except里面执行
	print('---------')
	try:
		content = f.read()
		print(content)
		f.close()
		print(a)
	except NameError as error1:  # 这里出错,就在这里拦截
		print('---:%s' % error1)

except FileNotFoundError as error:
	print('提示:%s' % error)

print('后续代码')

# 如果内层函数出现异常,默认由自己处理,如果它没有处理异常,会传到外层的try.
def test1():
	print('0000')  # 2
	print(num)
	print('llll')


def test2():
	try:
		print('00010') # 1
		test1()
		print('llll0')
	except:
		print('test2出现异常')  # 3

	print('333')  # 4


test2()
print('----')  # 5
