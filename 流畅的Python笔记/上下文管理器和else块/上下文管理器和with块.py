"""
上下文管理器对象存在的目的是管理with语句,就像迭代器的存在是为了管理for语句一样.


with语句的目的是简化try/finally模式.这种模式用于保证一段代码运行完毕后执行某项操作.即便那段代码由于异常,return语句或sys.exit()调用而中止,也会执行指定的操作.finally子句中的代码通常用于释放重要的资源,或者还原临时变更的状态.


上下文管理器协议包含__enter__和__exit__两个方法.with语句开始运行时,会在上下文管理器对象上调用__enter__方法.with语句运行结束之后,会在上下文管理器对象上面调用__exit__方法,以此扮演finally子句的角色.

最常见的例子是确保关闭文件对象.使用with语句关闭文件的详细说明参数示例:




with open("mirror.py") as fp:  # fp绑定到打开的文件上,因为文件的__enter__方法返回self
	src = fp.read(60)  # 从fp中读取一些数据.


示例15-1中标注1的那行代码道出了不易觉察但很重要的一点:执行with后面的表达式得到的结果是上下文管理器对象,不过,把值绑定到目标变量上(as子句)是在上下文管理器对象上调用__enter__方法的结果.

碰巧,示例15-1中的open()函数返回TextIOWrapper类的实例,而该实例的__enter__方法返回self.不过,__enter__方法除了返回上下文管理器之外,还可能返回其他对象.

不管控制流程以哪种方式退出with块,都会在上下文管理器对象上调用__exit__方法,而不是在__enter__方法返回的对象上调用.

with语句的as子句是可选的.对open函数来说,必须加上as子句,以便获取文件的引用.不过,有些上下文管理器会返回None,因为没什么有用的对能提供给用户.

from mirror import LookingGlass
with LookingGlass() as what:
	print("Alice,Kitty and Snowdrop")
	print(what)


中止和终止:
	
	中止:中途停止.
	终止:结束了,不再发展.


格式化符号	说明
%c	转换成字符（ASCII 码值，或者长度为一的字符串）
%r	优先用repr()函数进行字符串转换
%s	优先用str()函数进行字符串转换
%d / %i	转成有符号十进制数
%u	转成无符号十进制数
%o	转成无符号八进制数
%x / %X	转成无符号十六进制数（x / X 代表转换后的十六进制字符的大小写）
%e / %E	转成科学计数法（e / E控制输出e / E）
%f / %F	转成浮点数（小数部分自然截断）
%g / %G	%e和%f / %E和%F 的简写
%%	输出% （格式化字符串里面包括百分号，那么必须使用%%）



上下文管理器类的代码:
"""
class LookingGlass:

	def __enter__(self):  # 除了self之外,Python调用__enter__方法时不传入其他参数
		import sys
		self.original_write = sys.stdout.write  # 把原来的sys.stdout.write方法保存在一个实例属性中,供后面使用.
		sys.stdout.write = self.reverse_write  # 为sys.stdout.write打猴子补丁,替换成自己编写的方法.
		return "JABBERWOCKY"

	def reverse_write(self,text):
		"""这是用于取代sys.stdout.write的方法,把text参数的内容反转,然后调用原来的实现"""
		self.original_write(text[::-1])

	def __exit__(self,exc_type,exc_value,traceback):
		import sys
		sys.stdout.write = self.original_write
		if exc_type is ZeroDivisionError:
			print("Please DO NOT divide by zero!")
			return True
"""
在实际使用中,如果应用程序接管了标准输出,可能会暂时把sys.stdout换成类似文件的其他对象,然后再切换成原来的版本.contextlib.redirect_stdout上下文管理器就是这么做的:只需传入类似文件的对象,用于替代sys.stdout.

解释器调用__enter__方法时,除了隐式的self之外,不会传入任何参数.传给__exit__方法的三个参数列举如下:

exc_type

	异常类:(例如ZeroDivisionError)

exc_value
	
	异常实例.有时会有参数传给异常构造方法,例如错误消息,这些参数可以使用exc_value.args获取.

在try/finally语句的finally块中调用sys.exc_info(),得到的就是__exit__接收的这三个参数.鉴于with语句是为了取代大多数try/finally语句,而且通常需要调用sys.exc_info()来判断做什么清理工作,这种行为是合理的.


上下文管理器是相当新颖的特性,Python社区肯定还在不断寻找新的创意用法,大致如下:
	1.在sqlit3模块中用于管理事务.
	2.在threading模块中用于维护锁.
	3.为Decimal对象的算术运算设置环境.
	4.为了测试临时给对象打补丁.


标准库中还有个contextlib模块,提供一些实用工具.参见下一节.

"""