"""

"""


import time

DEFAULT_FMT = "[{elapsed:0.8f}s] {name}({args}) -> {result}"

def clock(fmt=DEFAULT_FMT):
	def decorate(func):
		def clocked(*_args):
			t0 = time.time()
			_result = func(*_args)
			elapsed = time.time() - t0
			name = func.__name__
			args = ",".join(repr(arg) for arg in _args)
			result = repr(_result)
			print(fmt.format(**locals()))
			return _result
		return clocked
	return decorate



if __name__ == '__main__':
	
	@clock()
	def snooze(seconds):
		time.sleep(seconds)


	for i in range(3):
		snooze(.123)



"""
输出:
[0.12304688s] snooze(0.123) -> None
[0.12304711s] snooze(0.123) -> None
[0.12304688s] snooze(0.123) -> None




讨论:装饰器最好通过实现__call__方法的类实现,不应该像本章的示例那样通过函数实现.

函数应该是黑盒,把实现隐藏起来,不让用户知道.但是对动态作用域来说,如果函数使用自由变量,
程序员必须知道函数的内部细节,这样才能搭建正确运行所需的环境.


词法作用域已成常态:根据定义函数的环境计算自由变量.词法作用域让人更难实现支持一等函数的语言,
因为需要支持闭包.不过,词法作用域让代码更易于阅读.

多年来,Python的lambda不支持闭包.从Python2.2开始修正了这个问题.



动态地给一个对象添加一些额外的职责,就扩展功能而言,装饰器比子类化更灵活.

装饰器与它所装饰的组件接口一致,因此它对使用该组件的客户透明.它将客户请求转发给该组件,并且可能在
转发前后执行一些额外的操作.透明性使得你可以递归嵌套多个装饰器,从而可以添加任意多的功能.



在Python中,装饰器函数相当于Decorator的具体子类,而装饰器返回的内部函数相当于装饰器实例.
返回的函数包装了被装饰的函数,这相当于装饰器设计模式中的组件.返回的函数式透明的,因为它接受相同的参数,
符合组件的接口.返回的函数把调用转发给组件,可以在转发前后执行额外的操作,因此,前面引用那段话的最后一句
可以改成:"透明性使得你可以递归嵌套多个装饰器,从而可以添加任意多的行为".这就是叠放装饰器的理论基础.
注意,我不是建议在Python程序中使用函数装饰器实现装饰器模式.在特定情况下确实可以这么做,但是一般来说,
实现"装饰器"模式最好使用类表示装饰器和要包装的组件.

"""