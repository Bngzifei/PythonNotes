"""
关系复杂了写del()方法,进行一个验证.

再试试:
"""

class Dog:
	def __init__(self):
		self.name = '322'

	# 做对象被删除前的临终遗言,验证对象是否被删除
	def __del__(self):  # 当对象即将被删除时,会自动调用.只要这个方法调用完了,这个对象就死了.就是del()方法走完了,对象就死了.
		print('%s走了' % self.name)


dog1 = Dog()
# a = dog1
del dog1  # 删了dog1的引用,但是还有一个a的引用 走了2次

# del a

# def main():
# 	dog1 = Dog()


# main()

print('---')  # 因为这个程序只有在执行完这一步之后才会将创建的dog1销毁,所以程序是先打印了---,然后才会调用del()方法销毁dog1.当先del()销毁dog1之后,程序时先销毁dog1,然后才打印---
