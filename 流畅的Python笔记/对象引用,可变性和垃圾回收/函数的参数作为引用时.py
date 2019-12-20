"""
Python唯一支持的参数传递模式是共享传参.多数面向对象语言都采用这一模式.

共享传参指函数的各个形式参数获得实参中各个引用的副本.也就是说,函数内部的
形参是实参的别名.

这种方案的结果是,函数可能会修改作为参数传入的可变对象,但是无法修改那些对象
的标识(即不能把一个对象替换成另一个对象)


函数可能会接收到的任何可变对象.

不要使用可变类型作为参数的默认值.

可选参数可以有默认值,装饰Python函数定义的一个很棒的特性,这样我们的API在进化的同时能保证向后兼容.然而,我们应该避免使用可变的对象作为参数的默认值.


出现这个问题的根源是,默认值在定义函数时计算(通常在加载模块时),因此默认值变成了函数对象的属性.因此,如果默认值是可变对象,而且修改了它的值,那么后续的函数调用都会受到影响.


可变默认值导致的这个问题说明了为什么通常使用None作为接收可变值的参数的默认值.


防御可变参数:如果定义的函数接收可变参数,应该谨慎考虑调用方是否期望修改传入的参数.

例如,如果函数接收一个字典,而且在处理的过程中要修改它,那么这个副作用要不要体现到函数外部?具体情况具体分析.这其实需要函数的编写者和调用方达成共识.


"""


class HauntedBus:
	"""备受幽灵乘客折磨的校车"""

	def __init__(self,passengers=[]):
		self.passengers = passengers

	def pick(self,name):
		self.passengers.append(name)

	def drop(self,name):
		self.passengers.remove(name)


bus1 = HauntedBus(["Alice","Bill"])
print(bus1.passengers)
bus1.pick("Charlie")
bus1.drop("Alice")
print(bus1.passengers)
bus2 = HauntedBus()
bus2.pick("Carrie")
print(bus2.passengers)
bus3 = HauntedBus()
bus3.passengers
bus3.pick("Dave")
print(bus2.passengers)
print(bus2.passengers is bus3.passengers)
print(bus1.passengers)

