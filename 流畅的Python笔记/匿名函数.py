"""
lambda 关键字在Python表达式内创建匿名函数

lambda函数的定义体中不能赋值,也不能使用while 和 try 等Python语句

在参数列表中最适合使用匿名函数.

除了作为参数传给高阶函数之外,Python很少使用匿名函数.由于句法上的限制,非平凡的
lambda表达式要么难以阅读,要么无法写出.


如果使用lambda表达式导致一段代码难以理解,建议像下面这样重构:
	
	1.>编写注释,说明lambda表达式的作用.

	2.>研究一会儿注释,并找出一个名词来概括注释.

	3.>把lambda表达式转换成def语句,使用那个名称来定义函数.

	4.>删除注释

lambda句法只是语法糖,与def语句一样,lambda表达式会创建函数对象.这是Python中
几种可调用对象的一种.


>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> sorted(fruits, key=lambda word: word[::-1])
['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']

注意这里的word就是前面fruits列表中的某一个元素.所表达的意思就是在fruits列表中
取出每个元素的逆序,然后进行排序输出为列表

"""