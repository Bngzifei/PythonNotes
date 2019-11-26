"""

GNU/Linux内核不理解Unicode,因此你可能发现了,对任何合理的编码方案来说,在文件名中使用字节序列都是无效的,
无法解码成字符串.在不同操作系统中使用各种客户端的文件服务器,在遇到这个问题时尤其容易出错.

为了规避这个问题,os模块中的所有函数,文件名或路径名参数既能使用字符串,也能使用字节序列.如果这样的函数使用
字符串参数调用,该参数会使用sys.getfileststemencoding()得到的编解码器自动编码,然后操作系统会使用相同的
编解码器解码.


一等函数:

	编程语言理论家把"一等对象"定义为满足下述条件的程序实体:

		1.在运行时创建

		2.能赋值给变量或数据结构中的元素

		3.能作为参数传给函数

		4.能作为函数的返回结果


函数式编程的特点之一是:使用高阶函数

	接受函数为参数,或者把函数作为结果返回的函数是高阶函数.
	map函数就是一例,此外,内置函数sorted也是:可选的key参数用于提供一个函数,它会应用到各个元素上进行排序.

>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> sorted(fruits, key=len)
['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']
>>>

任何单参数函数都能作为key参数的值.例如:为了创建押韵词典,可以把各个单词反过来拼写,然后排序.


在函数式编程范式中,最为人熟知的高阶函数有map,filter,reduce和apply.apply函数在Python2.3中标记为过时,在
Python3中移除了,因为不再需要它了.如果想使用不定量的参数调用函数,可以编写:
	fn(*args,**keywords),不用再编写apply(fn,args,kwargs)




map,filter,reduce的现代替代品

	函数式语言通常会提供map,filter和reduce三个高阶函数(有时使用不同的名称).在Python3中,map和filter还是内置函数,
	但是由于引入了列表推导和生成器表达式,它们变得没那么重要了.列表推导或生成器表达式具有map和filter两个函数的功能,
	而且更易于阅读.

在Python3中,map和filter返回生成器(一种迭代器),因此现在它们的直接替代品是生成器表达式(在Python2中,这两个函数返回列表,
因此最接近的替代品是列表推导.)

在Python2中,reduce是内置函数,但是在Python3中放到functools模块里了.这个函数最常用于求和.

sum和reduce的通用思想是把某个操作连续应用到序列的元素上,累计之前的结果,把一系列值规约成一个值.

all和any也是内置的归约函数.

all(iterable)
	
	如果iterable的每个元素都是真值,返回True,all([])返回True

any(iterable)
	
	只要iterable中有元素是真值,就返回True,any([])返回False

"""
