"""

首先要知道,yield from 是全新的语言结构.它的作用比yield多很多,因此人们认为继续使用那个关键字多少会引起误解.在其他语言中,类似的结构使用await关键字,这个名称好多了,因为它传达了至关重要的一点:在生成器gen中使用yield from subgen()时,subgen会获得控制权,把产出的值传给gen的调用方,即调用方可以直接控制subgen.与此同时,gen会阻塞,等待subgen终止.


yield from 可用于简化for循环中的yield表达式:
例如:
>>>def gen():
	for c in "AB":
		yield c
	for i in range(1,3):
		yield i

>>>list(gen())
["A","B",1,2]

可以改写为:
>>>def gen():
	yield from "AB"
	yield from range(1,3)
>>>list(gen())
["A","B",1,2]



使用yield from 链接可迭代的对象

def chain(*iterables):
	for it in iterables:
		yield from it

>>> s = "ABC"
>>> t = tuple(range(3))
>>> list(chain(s,t))
["A","B","C",0,1,2]


yield from x 表达式对x对象所做的第一件事是,调用iter(x),从中获取迭代器.因此,x可以是任何可迭代的对象.

可是,如果yield from结构唯一的作用是替代产出值的嵌套for循环,这个结构很有可能不会添加到Python语言中.yield from 结构的本质作用无法通过简单的可迭代对象说明.而要发散思维,使用嵌套的生成器.因此,引入yield from 结构的PEP 380才起了把职责委托给子生成器的句法这个标题.

yield from的主要功能是打开双向通道,把最外层的调用方与最内层的子生成器连接起来,这样二者可以直接发送和产出值,还可以直接传入异常,而不用在位于中间的协程中添加大量处理异常的样板代码.有了这个结构,协程可以通过以前不可能的方式委托职责.

若想使用yield from 结构,就要大幅改动代码.为了说明需要改动的部分,PEP380使用了一些专门的术语.


委派生成器:
	包含yield from <iterable>表打式的生成器函数

子生成器:
	从yield from表达式中<iterable>部分获取的生成器.

调用方:
	PEP380使用调用方这个术语指代调用委派生成器的客户端代码.在不同的语境中,我会使用"客户端"代替"调用方",以此与委派生成器(也是调用方,因为它调用了子生成器)区分开.

PEP380 经常使用"迭代器"这个词指代子生成器.这样会让人误解,因为委派生成器也是迭代器.因此,我选择使用"子生成器"这个术语,与PEP380的标题保持一致.然而,子生成器可能是简单的迭代器,只实现了__next__方法,但是,yield from也能处理这种子生成器.不过,引入yield from 结构的目的是为了支持实现了__next__,send,close,和throw方法的生成器.


委派生成器在yield from表达式处暂停时,调用方可以直接把数据发给子生成器,子生成器再把产出的值发给调用方.子生成器返回之后,解释器会抛出StopIteration异常,并把返回值附加到异常对象上,此时委派生成器会恢复.


使用yield from 计算平均值并输出统计报告:
"""

from collections import namedtuple

Result = namedtuple("Result","count average")

def averager():
	"""子生成器"""
	total = 0.0
	count = 0
	average = None
	while True:
		term = yield
		# 至关重要的终止条件.如果不这么做,使用yie;d from 调用这个协程的生成器会永远阻塞.
		if term is None:
			break

		total += term
		count += 1
		average = total/count
		# 返回的Result会成为grouper函数中yield from表达式的值.
		return Result(count,average)

def grouper(results,key):
	"""委派生成器"""
	while True:
		# grouper发送的每个值都会经由yield from处理,通过管道传给averager实例.grouper会在yield from 表达式处暂停,等待averager实例处理客户端发来的值.averager实例运行完毕后,返回的值绑定到results[key]上.while 循环会不断创建averager实例,处理更多的值.
		results[key] = yield from averager()


# main函数式客户端代码,是调用方.这是驱动一切的函数.
def main(data):
	"""客户端代码,即调用方"""
	results = {}
	for key,values in data.items():
		# group是调用grouper函数得到的生成器对象,传给grouper函数的第一个参数是results,用于搜集结果,第二个参数是某个键,group作为协程使用.
		group = grouper(results,key)
		next(group)  # 预激group协程
		for value in values:
			# 把各个value传给grouper.传入的值最终到达averager函数中term = yield那一行,grouper永远不知道传入的值是什么.
			group.send(value)  
		# 把None传入grouper,导致当前的averager实例终止,也让grouper继续运行,再创建一个averager实例,处理下一组值.
		group.send(None)

	report(results)


def report(results):
	"""输出报告"""
	for key,result in sorted(results.items()):
		group,unit = key.split(";")
		print("{:2} {:5} averager {:.2f}{}".format(result.count,group,result.average,unit))

data = {
	'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5], 
	'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43], 
	'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3], 
	'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
	main(data)


"""
示例展示了yield from结构最简单的用法,只有一个委派生成器和一个子生成器.因为委派生成器相当于管道,所以可以把任意数量个委派生成器连接在一起:一个委派生成器使用yield from调用一个子生成器,而那个子生成器本身也是委派生成器,使用yield from调用另一个子生成器,以此类推.最终这个链条要以一个只使用yield 表达式的简单生成器结束;不过,也能以任何可迭代的对象结束.


任何yield from链条都必须由客户驱动,在最外层委派生成器上调用next(...)函数或.send(...)方法.可以隐式调用,例如使用for循环.

"""

























