"""
当我在自己的程序中发现用到了模式,我觉得这就表明某个地方出错了.
程序的形式应该仅仅反映它所要解决的问题.代码中其他任何外加的形式都是一个信号,(至少对我来说)表明我对问题的抽象还不够深---这通常意味着自己正在手动完成的事情,本应该通过写代码来让宏的扩展自动实现.



迭代是数据处理的基石.扫描内存中放不下的数据集时,我们要找到一种惰性获取数据项的方式,即按需一次获取一个数据项.这就是迭代器模式.本章说明Python语言是如何内置迭代器模式的,这样就避免了自己手动去实现.



所有生成器都是迭代器,因为生成器完全实现了迭代器接口.不过,根据<<设计模式:可复用面向对象软件的基础>>一书的定义,迭代器用于从集合中取出元素;而生成器用于"凭空"生成元素.在Python社区中,大多数时候都把迭代器和生成器视作同一概念.

在Python3中,生成器有广泛的用途.现在,即使是内置的range()函数也返回一个类似生成器的对象,而以前则返回完整的列表.如果一定要让range()函数返回列表,那么必须明确指定,例如,list(range(100))

在Python中,所有集合都可以迭代.在Python语言内部,迭代器用于支持:

	for循环

	构建和扩展集合类型

	逐行遍历文本文件

	列表推导,字典推导和集合推导

	元组拆包

	调用函数时,使用*拆包实参



首先来研究iter(...)函数如何把序列变得可以迭代


sentence.py
"""
import re
import reprlib

RE_WORD = re.compile("\w+")


class Sentence:

	def __init__(self,text):
		self.text = text
		# re.findall函数返回一个字符串列表,里面的元素是正则表达式的全部非重叠匹配
		self.words = RE_WORD.findall(text)

	def __getitem__(self,index):
		return self.words[index]

	def __len__(self):
		return len(self.words)

	def __repr__(self):
		# reprlib.repr这个实用函数用于生成大型数据结构的简略字符串表示形式.默认情况下,reprlib.repr函数生成的字符串最多有30个字符.
		return "Sentence(%s)" % reprlib.repr(self.text)

"""
所有Python程序员都知道,序列可以迭代.

解释器需要迭代对象x时,会自动调用iter(x)

内置的iter函数有以下作用.

1.>检查对是否实现了__iter__方法,如果实现了就调用它,获取一个迭代器.

2.>如果没有实现__iter__方法,但是实现了__getitem__方法,Python会创建一个迭代器,尝试按顺序(从索引0开始)获取元素.

3.>如果尝试失败,Python抛出TypeError异常,通过会提示 C object is not iterable (C 对象不可迭代),其中C是目标对象所属的类.

任何Python序列都可迭代的原因是,它们都实现了__getitem__方法.其实,标准的序列也都实现了__iter__方法,因此你也应该这么做.之所以对__getitem__方法做特殊处理,是为了向后兼容.而未来可能不会再这么做.

从Python3.4开始,检查对象x能否迭代,最准确的方法是:调用iter(x)函数,如果不可迭代,再处理TypeError异常.这比使用isinstance(x,abc.Iterable)更准确,因为iter(x)函数会考虑到遗留的__getitem__方法.而abc.Iterable类则不考虑.

迭代对象之前显式检查对象是否可迭代或许没必要,毕竟尝试迭代不可迭代的对象时,Python抛出的异常信息很明确:TypeError:"C" object is not iterable.如果除了抛出TypeError异常之外还要做进一步的处理,可以使用try/except快,而无需显式检查.如果要保存对象,等以后再迭代,或许可以显式检查,因为这种情况可能需要尽早捕获错误.







"""


