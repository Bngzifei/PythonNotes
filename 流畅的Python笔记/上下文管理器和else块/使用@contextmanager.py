"""
@contextmanager装饰器能减少创建上下文管理器的样板代码量,因为不用编写一个完整的类,定义__enter__和__exit__方法,而只需实现一个yield语句的生成器,生成想让__enter__方法返回的值.

在使用@contextmanager装饰的生成器中,yield语句的作用是把函数的定义体分成两部分:yield语句前面的所有代码在with块开始时(即解释器调用__enter__方法时)执行,yield语句后面的代码在with块结束时(即调用__exit__方法时)执行.

下面举个例子.示例15-5使用一个生成器代替示例15-3中定义的LookingGlass类.

示例15-5 mirror_gen.py:使用生成器实现的上下文管理器

"""
import contextlib


@contextlib.contextmanager
def looking_glass():
	import sys
	original_write = sys.stdout.write  # 贮存原来的sys.stdout.write方法

	def reverse_write(text):  # 定义自定义的reverse_write函数:在闭包中可以访问original_write
		original_write(text[::-1])


	sys.stdout.write = reverse_write  # 把sys.stdout.write替换成reverse_write
	yield "ABBABBDBDB"  # 产出一个值,这个值会绑定到with语句中as子句的目标变量上.执行with块中的代码时,这个函数会在这一点暂停.
	sys.stdout.write = original_write  # 控制权一旦跳出with块,继续执行yield语句之后的代码;这里是恢复成原来的sys.stdout.write方法.

"""
示例15-6是使用looking_glass函数的例子
>>>from mirror_gen import looking_glass
>>>with looking_glass() as what:
	print("Alice,Kitty and Snowdrop")
	print("what")
>>> what

与示例15-2唯一的区别是上下文管理器的名字:LookingGlass变成了looking_glass

其实,contextlib.contextmanager装饰器会把函数包装成实现__enter__和__exit__方法的类.

这个类的__enter__方法有如下作用.

1.>调用生成器函数,保存生成器对象(这里把它称为gen)

2.>调用next(gen),执行到yield关键字所在的位置.

3.>返回next(gen)产出的值,以便把产出的值绑定到with/as语句中的目标变量上.

with终止时,__exit__方法会做以下几件事.

1.>检查有没有把异常传给exc_type;如果有,调用gen.throw(exception),在生成器函数定义体中包含yield关键字的那一行抛出异常.

2.>否则,调用next(gen),继续执行生成器函数定义体中yield语句之后的代码.

示例15-5有一个严重的错误:如果在with块中抛出了异常,Python解释器会将其捕获,然后在looking_glass函数的yield表达式里再次抛出.但是,那里没有处理错误的代码,因此looking_glass函数会中止,永远无法恢复成原来的sys.stdout.write方法,导致系统处于无效状态.

前面说过,为了告诉解释器异常已经处理了,__exit__方法会返回True,此时解释器会压制异常.如果__exit__方法没有显式返回一个值,那么解释器得到的是None,然后向上冒泡异常.使用@contextmanager装饰器时,默认的行为是相反的:装饰器提供的__exit__方法假定发给生成器的所有异常都得到处理了,因此应该压制异常.如果不想让@contextmanager压制异常,必须在被装饰的函数中显式重新抛出异常.

这样约定的原因是:创建上下文管理器时,生成器无法返回值,只能产出值.不过,现在可以返回值了.


使用@contextmanager装饰器时,要把yield语句放在try/finally语句中(或者放在with语句中),这是无法避免的,因为我们永远不知道上下文管理器的用户会在with块中做什么.


用于原地重写文件的上下文管理器:
"""
import csv

with inplace(csvfilename,"r",newline="") as (infh,outfh):
	reader = csv.reader(infh)
	writer = csv.writer(outfh)

	for row in reader:
		row += ["new","columns"]
		writer.writerow(row)


"""
inplace函数是个上下文管理器,为同一个文件提供了两个句柄(这个示例中的infh和outfh),以便同时读写同一个文件.这比标准库中的fileinput.input函数易于使用.


在此之前的所有代码都用于设置上下文:先创建备份文件,然后打开并产出__enter__方法返回的可读和可写文件句柄的引用.yield关键字之后的__exit__处理过程中把文件句柄关闭;如果什么地方出错了,那么从备份文中恢复文件.

注意,在@contextmanager装饰器装饰的生成器中,yield与迭代没有任何关系.在本节所举的示例中,生成器函数的作用更像是协程:执行到某一点时暂停,让客户代码执行,直到客户让协程继续做事.


本章小结:
	
	with不仅能管理资源,还能用于去掉常规的设置和清理代码,或者在另一个过程前后执行的操作.
	
	最后,我们分析了标准库中contextlib模块里的函数.其中,@contextmanager装饰器能把包含一个yield语句的简单生成器变成上下文管理器---这比定义一个至少包含两个方法的类要更简洁.
	
	@contextmanager装饰器优雅且实用,把三个不同的Python特性结合到了一起:函数装饰器,生成器和with语句.


编写了一个用于统计代码运行时间的上下文管理器,还编写了一个使用事务修改list对象的上下文管理器:在with块创建list实例的副本,所有改动都针对那个副本:仅当with块没有抛出异常,正常执行完毕之后,才用副本替代原来的列表.这样做简单又巧妙.


	with语句是非常了不起的特性.我建议你在实践中深挖这个特性的用途.使用with语句或许能做意义深远的事情.with语句最好的用法还未被发掘出来.我预料,如果有好的用法,其他语言以及未来的语言会借鉴这个特性.或许,你正在参与的事情几乎与子程序的发明一样意义深远.

"""